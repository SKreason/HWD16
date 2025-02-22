from django_filters import FilterSet, ModelChoiceFilter, OrderingFilter
from .models import Announcement


class RespondFilter(FilterSet):
    announcement = ModelChoiceFilter(
        queryset=Announcement.objects.all(),
        label='По объявлениям',
        empty_label='без фильтра',
    )

    def __init__(self, *args, **kwargs):
        super(RespondFilter, self).__init__(*args, **kwargs)
        self.filters['announcement'].queryset = Announcement.objects.filter(author=kwargs['request'])

