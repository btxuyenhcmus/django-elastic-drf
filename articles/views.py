from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from articles import documents as articles_documents
from articles import serializers as articles_serializers


class ArticleViewSet(DocumentViewSet):
    document = articles_documents.ArticleDocument
    serializer_class = articles_serializers.ArticleDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'title',
        'body',
    )

    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title.raw',
        'body': 'body.raw',
        'author': {
            'field': 'author_id',
            'lookups': [
                LOOKUP_QUERY_IN,
            ]
        },
        'created': 'created',
        'modified': 'modified',
        'pub_date': 'pub_date',
    }

    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'author': 'author_id',
        'created': 'created',
        'modified': 'modified',
        'pub_date': 'pub_date',
    }

    # Specify default ordering
    ordering = ('id', 'created',)

    # Suggester fields
    suggester_fields = {
        'title_suggest': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }