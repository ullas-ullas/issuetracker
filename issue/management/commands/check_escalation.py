from django.core.management.base import BaseCommand
from django.utils import timezone
from issue.models import Issue

class Command(BaseCommand):
    help = "escalation logic"

    def handle(self, *args, **kwargs):
        issues = Issue.objects.filter(is_escalated=False, status__in = ["OPEN", "IN_PROGRESS"],due_time__isnull=False)
        count = 0
        if issues:            
            for issue in issues:
                if timezone.now() > issue.due_time:
                    issue.is_escalated = True
                    issue.priority = "HIGH"
                    issue.save()
                    count+=1

        if issues:
            self.stdout.write(f"{count} issues escalated")
        else:
            self.stdout.write(f"no Issues found")