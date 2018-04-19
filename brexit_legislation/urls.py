from django.conf.urls import include, url

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^api/', include('api.urls')),
    url(r'^browse/', include('browse.urls')),
    url(r'^search/', include('search.urls')),
]
