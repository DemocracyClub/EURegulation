from django.conf.urls import url

from .views import (
    SingleRegulationView, SingleKeywordView, RegulationYearView, BrowseHome)

urlpatterns = [
    url(
        r'^$',
        BrowseHome.as_view(),
        name="browse_home_view"
    ),
    url(
        r'^regulation/(?P<year>[0-9]+)/(?P<celex_number>[^/]+)/',
        SingleRegulationView.as_view(),
        name="single_regulation_view"
    ),
    url(
        r'^regulation/(?P<year>[0-9]+)/',
        RegulationYearView.as_view(),
        name="regulation_year_view"
    ),
    url(
        r'^keyword/(?P<keyword>.*)/',
        SingleKeywordView.as_view(),
        name="single_keyword_view"
    ),
]
