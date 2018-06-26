from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import SearchByDocumentForm
from .more_like_text_helper import more_like_text


@method_decorator(csrf_exempt, name='dispatch')
class SearchView(TemplateView):
    template_name = "search/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['form'] = SearchByDocumentForm(self.request.POST)
        if context['form'].is_valid():
            text = context['form'].cleaned_data['document_text']
            context['results'] = more_like_text(text)
        return context

    def post(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)
