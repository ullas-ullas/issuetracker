from django.shortcuts import render
from rest_framework import viewsets
from .serializer import IssueSerializer
from .models import Issue

# Create your views here.

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'USER':
            return Issue.objects.filter(created_by = user)
        elif user.role == 'STAFF':
            return Issue.objects.filter(department = user.dept)
        elif user.role == "SUPERVISOR":
            return Issue.objects.filter(is_escalated = True)

        return Issue.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)