from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Case, Value, When, IntegerField
import re

from .helper.englishtopinyin import *
from .models import Entries
from .serializers import EntriesSerializer



class FilteredViewSet(viewsets.ModelViewSet):
    serializer_class = EntriesSerializer
    def get_queryset(self):
        queryset = Entries.objects.all()
        filter_value = self.request.query_params.get('english', None)
        print(f"line 16 FILTER VALUE: {filter_value}")

        filter_value = add_pinyin_numbers(convert_ipa_string_to_pinyin(replace_non_compatible_ipa(convert_english_to_ipa(filter_value))))
        print(filter_value)
        # for word in pin:
            # filter_value = word
        try:
            if filter_value is not None:
                cases = [When(pinyin=x, then=Value(i)) for i, x in enumerate(filter_value)] 
                case = Case(*cases, output_field=IntegerField())
                queryset = queryset.filter(pinyin__in=filter_value)
                queryset = queryset.annotate(my_order=case).order_by('my_order')
                # queryset = queryset.filter(pinyin__in=filter_value)
                return queryset
        except:
             if filter_value is not None:
                cases = [When(pinyin=x, then=Value(i)) for i, x in enumerate(filter_value)] 
                case = Case(*cases, output_field=IntegerField())
                queryset = queryset.filter(pinyin__in=filter_value)
                queryset = queryset.annotate(my_order=case).order_by('my_order')
                # queryset = queryset.filter(pinyin__in=filter_value)
                return queryset



