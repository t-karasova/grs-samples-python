from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""
default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"


# [START get_search_service_client]
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# [END get_search_service_client]

# [START get_search_request_for_the_first_page]
def get_search_request_first_page(query: str, page_size: int):
    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.page_size = page_size
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors

    print("---search_request:---")
    print(search_request)

    return search_request


# [END get_search_request_for_the_first_page]

# [START get_search_request_for_the_next_page]
def get_search_request_next_page(query: str, page_size: int, page_token: str):
    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.page_size = page_size
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors
    search_request.page_token = page_token

    print("---search_request:---")
    print(search_request)

    return search_request


# [END get_search_request_for_the_next_page]

# [START search_for_products_with_pagination_next_page_token]
def search():
    search_request_first_page = get_search_request_first_page("Nest_Maxi", 1)
    search_first_page_response = get_search_service_client().search(search_request_first_page)
    print("---next page token from the first page:---")
    print(search_first_page_response.next_page_token)

    next_page_token = search_first_page_response.next_page_token
    search_request_next_page = get_search_request_next_page("Nest_Maxi", 1, next_page_token)
    search_response = get_search_service_client().search(search_request_next_page)

    print("---search results from the next page---")
    print(search_response)


# [END search_for_products_with_pagination_next_page_token]

search()
