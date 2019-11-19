from django.urls import path, include
from .views import EntriesViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PinyinSimplifiedViewSet, basename='entries')
urlpatterns = router.urls