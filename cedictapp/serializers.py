from rest_framework import serializers
from .models import Entries

class EntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ['traditional', 'simplified', 'pinyin', 'english']