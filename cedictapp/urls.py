from django.urls import path, include
from .views import PinyinViewSet, SimpleViewSet, TraditionalViewset, EnglishViewset # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pinyin', PinyinViewSet, basename='pinyin')
router.register(r'simple', SimpleViewSet, basename='simple')
router.register(r'traditional', TraditionalViewSet, basename='traditional')
router.register(r'english', EnglishViewSet, basename='english')
urlpatterns = router.urls