import django_filters

from .models import GroupTour

class GroupTourFilter(django_filters.FilterSet):
    class Meta:
        model = GroupTour
        fields = ('from_city',)
