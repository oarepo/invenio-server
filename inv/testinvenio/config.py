from flask import request
from invenio_indexer.api import RecordIndexer
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all
from invenio_search import RecordsSearch
#from oarepo_ui import translate_facets, translate_filters

from testinvenio.records import TestRecord


def loader():
  return request.json


RECORDS_REST_ENDPOINTS = {
  'testinvenio-records':
    dict(
      pid_type='recid',
      pid_minter='recid',
      pid_fetcher='recid',
      default_endpoint_prefix=True,
      record_class=TestRecord,
      search_class=RecordsSearch,
      indexer_class=RecordIndexer,
      search_index='testinvenio-record',
      search_type=None,
      record_serializers={
        'application/json': 'invenio_records_rest.serializers:json_v1_response',
      },
      record_loaders={
        'application/json': loader
      },
      search_serializers={
        'application/json': 'invenio_records_rest.serializers:json_v1_search',
      },
      list_route='/records/',
      item_route='/records///<pid(recid,record_class="testinvenio.records.TestRecord"):pid_value>',
      default_media_type='application/json',
      max_result_window=10000,
      create_permission_factory_imp=allow_all,
      error_handlers=dict(),
    )
}

INDEXER_RECORD_TO_INDEX = 'testinvenio.ext:record_to_index'

FILTERS = {
  # object
  'category': terms_filter('category'),
}

def term_facet(field, order='desc', size=100):
    return {
        'terms': {
            'field': field,
            'size': size,
            "order": {"_count": order}
        },
    }


FACETS = {
  # object
  'category': term_facet('category'),
}

RECORDS_REST_FACETS = {
    'testinvenio-records': {
        'aggs': FACETS, #translate_facets(FACETS, label='{facet_key}', value='{value_key}'),
        'filters': FILTERS #translate_filters(FILTERS, label='{filter_key}')
    },
}
