from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets

class PinyinViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.values_list('id', 'pinyin')
    serializer_class = EntriesSerializer

class SimplifiedViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.values_list('id', 'simplified')
    serializer_class = EntriesSerializer

class TraditionalViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.values_list('id', 'traditional')
    serializer_class = EntriesSerializer

class EnglishViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.values_list('id', 'english')
    serializer_class = EntriesSerializer

