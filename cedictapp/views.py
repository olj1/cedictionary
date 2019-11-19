from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets

class PinyinSimplifiedViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.values_list('pinyin', 'simplified')
    serializer_class = EntriesSerializer


