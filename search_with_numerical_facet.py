import random
import string

from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest, Interval

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


# [START search_product_with_numerical_facet]
def search_products_numerical_facet(query: str, key: str, intervals: [Interval], page_size=10):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_key.intervals = intervals
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.facet_specs = [facet_spec]
    search_request.page_size = page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_numerical_facet]


def search():
    setup_catalog.ingest_products(test_id)

    interval = Interval()
    interval.minimum = 10.0
    interval.exclusive_maximum = 20.0
    search_response = search_products_numerical_facet(title_query, "price", [interval])
    print("---numerical facet search response---")
    print(search_response)

    setup_catalog.delete_products()


search()
