import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class MemberFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="Date_start", lookup_expr='gte')

    Fname= CharFilter(field_name='FirstName', lookup_expr='icontains')
    Lname = CharFilter(field_name='LastName', lookup_expr='icontains')
    class Meta:
        model = Members
        fields = '__all__'
