from django.shortcuts import render

from .models import Entries
from .serializers import EntriesSerializer
from rest_framework import viewsets

class EntriesViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.all()
    serializer_class = EntriesSerializer
