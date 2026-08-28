class TriageResponse {
  final String category;
  final String priority;
  final String action;
  final bool clarificationNeeded;
  final String? model;
  final String? error;

  TriageResponse({
    required this.category,
    required this.priority,
    required this.action,
    required this.clarificationNeeded,
    this.model,
    this.error,
  });

  /// Convert JSON map into a typed Dart object.
  /// Missing fields get safe default values so the app does not crash.
  factory TriageResponse.fromJson(Map<String, dynamic> json) {
    return TriageResponse(
      category: json['category'] as String? ?? 'other',
      priority: json['priority'] as String? ?? 'low',
      action: json['action'] as String? ?? 'No action available',
      clarificationNeeded: json['clarification_needed'] as bool? ?? false,
      model: json['model'] as String?,
      error: json['error'] as String?,
    );
  }

  /// Helpful for debugging
  @override
  String toString() {
    return 'TriageResponse(category: $category, priority: $priority, '
        'action: $action, clarificationNeeded: $clarificationNeeded)';
  }
}
