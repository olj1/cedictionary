from django.urls import path, include, patterns
from .views import FilteredViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FilteredViewSet, basename='pinyin')
urlpatterns = patterns('', url(r'^', include(router.urls)))