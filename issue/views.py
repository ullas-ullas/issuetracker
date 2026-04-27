from django.shortcuts import render
from rest_framework import viewsets
from .serializer import IssueSerializer
from .models import Issue
from datetime import timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

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

    def update(self, request, *args, **kwargs):
        issue = self.get_object()

        if request.user.role == "USER":
            return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)

        if "assigned_to" in request.data:
            if request.user.role != "STAFF":
                return Response({"error": "Only staff can assign"}, status.HTTP_403_FORBIDDEN)

            if request.user.department != issue.department:
                return Response({"error": "Wrong department"}, status.HTTP_403_FORBIDDEN)

        if "status" in request.data:
            if request.user.role != "STAFF":
                return Response({"error": "Only staff can update status"}, status.HTTP_403_FORBIDDEN)

            if issue.assigned_to != request.user:
                return Response({"error": "Not assigned to you"}, status.HTTP_403_FORBIDDEN)

        if "priority" in request.data:
            if request.user.role != "SUPERVISOR":
                return Response({"error": "Only supervisor can set priority"}, status.HTTP_403_FORBIDDEN)

        if "is_escalated" in request.data:
            return Response({"error": "Not allowed"}, status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user, due_time = timezone.now()+timedelta(hours=48))