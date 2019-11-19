from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets

class FilteredViewSet(viewsets.ModelViewSet):
    serializer_class = EntriesSerializer
    def get_queryset(self):
        return Entries.objects.filter(pinyin=self.kwargs['pinyin'])


# class SimplifiedViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'simplified')
#     serializer_class = EntriesSerializer

# class TraditionalViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'traditional')
#     serializer_class = EntriesSerializer

# class EnglishViewSet(viewsets.ModelViewSet):
#     queryset = Entries.objects.values_list('id', 'english')
#     serializer_class = EntriesSerializer

