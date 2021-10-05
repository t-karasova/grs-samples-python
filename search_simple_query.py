import os
import random
import string
import setup_catalog

from google.api_core.client_options import ClientOptions

from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

project_number = "1038874412926"
endpoint = "retail.googleapis.com"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_search_placement = "projects/1038874412926/locations/global/catalogs/default_catalog/placements/default_search"


def get_search_service_client():
    client_options = ClientOptions(endpoint)
    return SearchServiceClient(client_options=client_options)


# [END search_client]

# [START search_product]
def search_products(query: str):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.visitor_id = visitor_id
    print("---search_request:---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product]

def search():
    setup_catalog.ingest_products(test_id)

    search_response = search_products(title_query)
    print("---search response---")
    print(search_response)

    setup_catalog.delete_products()


search()
