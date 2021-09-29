import os
import random
import string
import setup_catalog

from google.api_core.client_options import ClientOptions

from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/Tatiana/GRS/token.json"
project_number = "1038874412926"
endpoint = "retail.googleapis.com"
isolation_filter_key = "INTEGRATION_FILTER_KEY"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/0".format(project_number)
default_search_placement = "projects/1038874412926/locations/global/catalogs/default_catalog/placements/default_search"


def get_search_service_client():
    client_options = ClientOptions(endpoint)
    return SearchServiceClient(client_options=client_options)


# [END search_client]


def build_isolation_filter(test__id: str):
    return 'attributes.{0}: ANY("{1}")'.format(isolation_filter_key, test__id)


# [START search_product_with_query_expansion_spec]
def search_products_with_query_expansion(query: str, _condition: SearchRequest.QueryExpansionSpec.Condition):
    query_expansion_spec = SearchRequest().QueryExpansionSpec()
    query_expansion_spec.condition = _condition

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.visitor_id = visitor_id
    search_request.query_expansion_spec = query_expansion_spec
    print("---search_request:---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_query_expansion_spec]


def search():
    setup_catalog.ingest_products(test_id)

    search_response = search_products_with_query_expansion(title_query, SearchRequest.QueryExpansionSpec.Condition.AUTO)
    print("QUERY EXPANSION SEARCH RESULTS")
    print(search_response.results)

    setup_catalog.delete_products()


search()
