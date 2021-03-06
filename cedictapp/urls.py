from django.urls import path, include
from django.conf.urls import url
from .views import FilteredViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'', FilteredViewSet, basename='english')
urlpatterns = [url(r'^', include(router.urls))]