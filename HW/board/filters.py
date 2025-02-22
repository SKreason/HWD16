from django_filters import FilterSet, ModelChoiceFilter
from .models import Announcement


class RespondFilter(FilterSet):
    """
    Фильтр для личной страницы откликов. Получаем queryset всех объявлений.
    """
    announcement = ModelChoiceFilter(
        queryset=Announcement.objects.all(),
        label='По объявлениям',
        empty_label='без фильтра',
    )

    def __init__(self, *args, **kwargs):
        """
        Заменяем на queryset с фильтром.
        """
        super(RespondFilter, self).__init__(*args, **kwargs)
        self.filters['announcement'].queryset = Announcement.objects.filter(author=kwargs['request'])

