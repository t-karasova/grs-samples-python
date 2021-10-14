from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""


# [START get_search_service_client]
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# [END get_search_service_client]

# [START get_search_request_with_ordering]
def get_search_request(query: str, order: str):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.order_by = order
    search_request.visitor_id = "123456"  # A unique identifier to track visitors

    print("---search request---")
    print(search_request)

    return search_request


# [END get_search_request_with_ordering]

# [START search_for_products_with_ordering]
def search():
    # TRY DIFFERENT ORDERING EXPRESSIONS HERE:
    order = 'price desc'

    search_request = get_search_request("Nest_Maxi", order)
    search_response = get_search_service_client().search(search_request)

    print("---ordered search results---")
    print(search_response)


# [END search_for_products_with_ordering]

search()
