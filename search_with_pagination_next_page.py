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


# [START search_product_with_page_size]
def search_products_with_page_size(query: str, _page_size: int):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.page_size = _page_size
    search_request.visitor_id = visitor_id
    print("---search_request:---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_page_size]

# [START search_product_with_page_token]
def search_products_with_page_token(query: str, _page_size: int, _page_token: str):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.page_size = _page_size
    search_request.page_token = _page_token
    search_request.visitor_id = visitor_id
    print("---search_request:---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_page_token]

def search():
    setup_catalog.ingest_products(test_id)

    search_response = search_products_with_page_size(title_query, 1)
    print("---page size search results---")
    print(search_response)

    next_page_token = search_response.next_page_token
    search_response = search_products_with_page_token(title_query, 1, next_page_token)
    print("---next page search results---")
    print(search_response)

    setup_catalog.delete_products()


search()
