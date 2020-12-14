from rest_framework.routers import DefaultRouter

from .viewsets import QuestionsViewSet

router = DefaultRouter()

router.register(r'questions', QuestionsViewSet, basename='questions')

urlpatterns = router.urls
