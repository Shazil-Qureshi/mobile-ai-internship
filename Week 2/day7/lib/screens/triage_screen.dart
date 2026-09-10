import 'package:flutter/material.dart';
import '../models/triage_response.dart';
import '../services/ai_service.dart';

class TriageScreen extends StatefulWidget {
  const TriageScreen({super.key});

  @override
  State<TriageScreen> createState() => _TriageScreenState();
}

class _TriageScreenState extends State<TriageScreen> {
  final TextEditingController _controller = TextEditingController();
  final AiService _aiService = AiService();

  bool _isLoading = false;
  TriageResponse? _result;
  String? _errorMessage;

  Future<void> _submit() async {
    final text = _controller.text.trim();

    if (text.isEmpty) {
      setState(() {
        _result = null;
        _errorMessage = 'Please enter a message';
      });
      return;
    }

    setState(() {
      _isLoading = true;
      _result = null;
      _errorMessage = null;
    });

    // Using mock for offline demo. Change to _aiService.classify(text)
    // when your backend is running.
    final response = await _aiService.classifyMock(text);

    setState(() {
      _isLoading = false;
      if (response.error != null && response.error != 'empty_input') {
        _errorMessage = response.action;
        _result = response;
      } else {
        _result = response;
        _errorMessage = null;
      }
    });
  }

  Color _priorityColor(String priority) {
    switch (priority.toLowerCase()) {
      case 'high':
        return Colors.red.shade400;
      case 'medium':
        return Colors.orange.shade400;
      default:
        return Colors.green.shade400;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Support Triage'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Describe your issue',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
            ),
            const SizedBox(height: 8),
            TextField(
              controller: _controller,
              maxLines: 4,
              decoration: InputDecoration(
                hintText: 'e.g. My payment failed and I need help',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _isLoading ? null : _submit,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 14),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              child: _isLoading
                  ? const SizedBox(
                      height: 20,
                      width: 20,
                      child: CircularProgressIndicator(strokeWidth: 2),
                    )
                  : const Text('Submit', style: TextStyle(fontSize: 16)),
            ),
            const SizedBox(height: 24),

            // Loading state
            if (_isLoading)
              const Center(
                child: Column(
                  children: [
                    CircularProgressIndicator(),
                    SizedBox(height: 12),
                    Text('Analyzing your message...'),
                  ],
                ),
              ),

            // Error state
            if (_errorMessage != null && !_isLoading)
              Card(
                color: Colors.red.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Row(
                    children: [
                      Icon(Icons.error_outline, color: Colors.red.shade700),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          _errorMessage!,
                          style: TextStyle(color: Colors.red.shade700),
                        ),
                      ),
                    ],
                  ),
                ),
              ),

            // Success / Result state
            if (_result != null && !_isLoading)
              Card(
                elevation: 2,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          const Text(
                            'Result',
                            style: TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const Spacer(),
                          Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 10,
                              vertical: 4,
                            ),
                            decoration: BoxDecoration(
                              color: _priorityColor(_result!.priority),
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              _result!.priority.toUpperCase(),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),
                      _buildRow('Category', _result!.category),
                      _buildRow('Action', _result!.action),
                      _buildRow(
                        'Clarification needed',
                        _result!.clarificationNeeded ? 'Yes' : 'No',
                      ),
                      if (_result!.model != null)
                        _buildRow('Model', _result!.model!),
                    ],
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 140,
            child: Text(
              label,
              style: TextStyle(
                color: Colors.grey.shade600,
                fontWeight: FontWeight.w500,
              ),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: const TextStyle(fontWeight: FontWeight.w600),
            ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
