
import datetime
from haystack import indexes
from .models import Regulation


class RegulationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # keywords = indexes.CharField(model_attr='keywords')
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Regulation

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
