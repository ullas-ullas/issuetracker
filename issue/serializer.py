from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):
    model = Issue
    fields = "__all__"
    read_only_fields = ["created_by", "status", "priority", "is_escalated", "created_at", "updated_at"]