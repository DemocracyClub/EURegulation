from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Count

from regulations.models import Regulation, Keyword

class BrowseHome(TemplateView):
    template_name = "browse_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulation'] = {}
        context['regulation']['years'] = Regulation.objects.all().values('year').annotate(total=Count('year')).order_by('year')
        return context


class RegulationYearView(ListView):
    def get_queryset(self):
        return Regulation.objects.filter(
            year=self.kwargs['year'],
        )

class SingleRegulationView(DetailView):
    def get_object(self):
        return Regulation.objects.get(
            celex_number=self.kwargs['celex_number']
        )

class SingleKeywordView(DetailView):
    slug_field = 'keyword'
    slug_url_kwarg = 'keyword'
    queryset = Keyword.objects.all()
