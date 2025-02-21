from django_filters import FilterSet, ModelChoiceFilter, OrderingFilter
from .models import Announcement


class RespondFilter(FilterSet):
    title = ModelChoiceFilter(
        queryset=Announcement.objects.all(),
        label='По объявлениям',
        empty_label='без фильтра',
    )

    def __init__(self, *args, **kwargs):
        super(RespondFilter, self).__init__(*args, **kwargs)
        self.filters.queryset = Announcement.objects.filter(author=kwargs['request'])

