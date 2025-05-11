from django_filters.rest_framework import FilterSet
from .models import *


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            '': ['exact'],
            'price': ['gt', 'lt'],
            'department': ['exact']
        }