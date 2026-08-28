import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/triage_response.dart';

/// Service layer that talks to the backend.
/// IMPORTANT: No API keys are stored here.
class AiService {
  // Change this URL when your backend is running.
  // For local testing you can point it to a mock or leave it as is.
  final String baseUrl;

  AiService({this.baseUrl = 'http://127.0.0.1:8000'});

  /// Sends user message to backend and returns a typed TriageResponse.
  Future<TriageResponse> classify(String userMessage) async {
    if (userMessage.trim().isEmpty) {
      return TriageResponse(
        category: 'other',
        priority: 'low',
        action: 'Please enter a message',
        clarificationNeeded: true,
        error: 'empty_input',
      );
    }

    try {
      final response = await http
          .post(
            Uri.parse('$baseUrl/triage'),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'user_message': userMessage}),
          )
          .timeout(const Duration(seconds: 15));

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = jsonDecode(response.body);
        return TriageResponse.fromJson(data);
      } else {
        return TriageResponse(
          category: 'other',
          priority: 'low',
          action: 'Server returned an error. Please try again.',
          clarificationNeeded: true,
          error: 'server_error_${response.statusCode}',
        );
      }
    } on FormatException {
      // Malformed JSON from backend
      return TriageResponse(
        category: 'other',
        priority: 'low',
        action: 'Received invalid response from server.',
        clarificationNeeded: true,
        error: 'malformed_response',
      );
    } catch (e) {
      // Network error, timeout, etc.
      return TriageResponse(
        category: 'other',
        priority: 'low',
        action: 'Network error. Please check your connection.',
        clarificationNeeded: true,
        error: 'network_error',
      );
    }
  }

  /// Mock version for offline testing (no real backend needed).
  /// This uses the same logic as the Day 6 mock provider.
  Future<TriageResponse> classifyMock(String userMessage) async {
    await Future.delayed(const Duration(milliseconds: 800)); // simulate network

    final lower = userMessage.toLowerCase();

    if (lower.contains('payment') ||
        lower.contains('refund') ||
        lower.contains('charged')) {
      return TriageResponse(
        category: 'billing',
        priority: 'high',
        action: 'Investigate payment issue',
        clarificationNeeded: false,
        model: 'mock-triage-v1',
      );
    } else if (lower.contains('login') ||
        lower.contains('password') ||
        lower.contains('account')) {
      return TriageResponse(
        category: 'account',
        priority: 'medium',
        action: 'Send password reset link',
        clarificationNeeded: false,
        model: 'mock-triage-v1',
      );
    } else if (lower.contains('crash') ||
        lower.contains('error') ||
        lower.contains('not working')) {
      return TriageResponse(
        category: 'technical',
        priority: 'high',
        action: 'Escalate to engineering team',
        clarificationNeeded: false,
        model: 'mock-triage-v1',
      );
    } else {
      return TriageResponse(
        category: 'other',
        priority: 'low',
        action: 'Request more details from user',
        clarificationNeeded: true,
        model: 'mock-triage-v1',
      );
    }
  }
}
