import random
import string

from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

import setup_catalog

project_number = "SET HERE VALID PROJECT NUMBER"
endpoint = "retail.googleapis.com"
isolation_filter_key = "INTEGRATION_FILTER_KEY"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_search_placement = "projects" + project_number + "locations/global/catalogs/default_catalog/placements/default_search"


def get_search_service_client():
    client_options = ClientOptions(endpoint)
    return SearchServiceClient(client_options=client_options)


# [END search_client]


def build_isolation_filter(test__id: str):
    return 'attributes.{0}: ANY("{1}")'.format(isolation_filter_key, test__id)


# [START search_product_with_textual_facet_excluded_filter_keys]
def search_products_textual_facet_excluded_filter_keys(query: str, key: str, excluded_filter_keys: [str], _filter: str):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key
    facet_spec.excluded_filter_keys = excluded_filter_keys

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.filter = '{0} AND {1}'.format(build_isolation_filter(test_id), _filter)
    search_request.facet_specs = [facet_spec]
    search_request.visitor_id = visitor_id
    print("---search request---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_textual_facet_excluded_filter_keys]


def search():
    setup_catalog.ingest_products(test_id)

    search_response = search_products_textual_facet_excluded_filter_keys(title_query, "colorFamily", ["colorFamily"],
                                                                         'colorFamily: ANY("black")')
    print("---excluded filter key facet search result---")
    print(search_response)

    setup_catalog.delete_products()


search()
