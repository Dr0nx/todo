from django_filters import rest_framework as filters
from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = ['created_at', 'project']

    # Range: Comments added between 2016-01-01 and 2016-02-01
    # f = F({'date_after': '2016-01-01', 'date_before': '2016-02-01'})
