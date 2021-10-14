from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""


# [START get_search_service_client]
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# [END get_search_service_client]

# [START get_search_request_with_page_size]
def get_search_request(query: str, page_size: int):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.page_size = page_size
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors

    print("---search_request:---")
    print(search_request)

    return search_request


# [END get_search_request_with_page_size]


# [START search_for_products_with_page_size]
def search():
    search_request = get_search_request("Nest_Maxi", 12)
    search_response = get_search_service_client().search(search_request)

    print("---page size search results---")
    print(search_response)


# [END search_for_products_with_page_size]

search()
