from django.conf.urls import url, include
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
import django_filters

from rest_framework.reverse import reverse

from rest_framework_nested import routers

from regulations.models import Regulation, Subject, Keyword


class KeywordSerializer(serializers.StringRelatedField):
    class Meta:
        model = Keyword
        fields = ('keyword',)


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'pk', 'subject',)


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class RegulationSerializer(serializers.HyperlinkedModelSerializer):
    subjects = SubjectSerializer(many=True)
    keywords = KeywordSerializer(many=True)
    html = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = Regulation
        fields = (
            'celex_number',
            'DC_description',
            'DC_identifier',
            'DC_language',
            'DC_publisher',
            'DC_source',
            'DC_subject',
            'DC_title',
            'DC_type',
            'html',
            'keywords',
            'number',
            'subjects',
            'text',
            'title',
            'url',
            'uuid',
            'year',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }

    def get_html(self, obj):
        return reverse(
            'regulation-html',
            kwargs={'uuid': obj.uuid},
            request=self.context['view'].request
        )

    def get_text(self, obj):
        return reverse(
            'regulation-text',
            kwargs={'uuid': obj.uuid},
            request=self.context['view'].request
        )


class RegulationFilter(FilterSet):
    keyword = django_filters.CharFilter(
        name="keywords__keyword", label="Keyword")

    class Meta:
        model = Regulation
        fields = ['celex_number', 'number', 'year', 'keyword']


# ViewSets define the view behavior.
class RegulationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Regulation.objects.all()
    serializer_class = RegulationSerializer
    lookup_field = 'uuid'
    filter_backends = (DjangoFilterBackend, )
    filter_class = RegulationFilter

    @detail_route(methods=['get'],)
    def html(self, request, uuid=None):
        return HttpResponse(self.get_object().body_html)

    @detail_route(methods=['get'],)
    def text(self, request, uuid=None):
        return HttpResponse(self.get_object().body_text)



router = routers.DefaultRouter()
router.register(r'regulation', RegulationViewSet)
router.register(r'subjects', SubjectViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
