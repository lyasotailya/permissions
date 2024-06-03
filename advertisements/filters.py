from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = filters.DateFromToRangeFilter()
    status = filters.CharFilter()
    creator = filters.NumberFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'creator', 'created_at',]