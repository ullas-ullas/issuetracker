from rest_framework import routers
from .views import IssueViewSet

router = routers.DefaultRouter()

router.register(r'issues', IssueViewSet, basename='issue')

urlpatterns = router.urls