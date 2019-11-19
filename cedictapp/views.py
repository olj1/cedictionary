from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets
import re

class FilteredViewSet(viewsets.ModelViewSet):
    serializer_class = EntriesSerializer
    def get_queryset(self):
        queryset = Entries.objects.all()
        filter_value = self.request.query_params.get('pinyin', None)
        if filter_value is not None:
            queryset = queryset.filter(pinyin=filter_value)
            return queryset


# class SimplifiedViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'simplified')
#     serializer_class = EntriesSerializer

# class TraditionalViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'traditional')
#     serializer_class = EntriesSerializer

# class EnglishViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'english')
#     serializer_class = EntriesSerializer

