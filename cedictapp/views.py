from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets
import re



class FilteredViewSet(viewsets.ModelViewSet):
    serializer_class = EntriesSerializer
    def get_queryset(self):
        queryset = Entries.objects.all()
        filter_value = self.request.query_params.get('english', None)


        print(f"FILTER VALUE: {filter_value}")
        if filter_value is not None:
            queryset = queryset.filter(pinyin=filter_value)
            return queryset



