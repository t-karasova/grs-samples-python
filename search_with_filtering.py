from google.api_core.client_options import ClientOptions

from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""


# Get search service client
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# Get Search Request with filter]
def get_search_request(query: str, _filter: str, page_size=10):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.filter = _filter
    search_request.page_size = page_size
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors

    print("---search_request:---")
    print(search_request)

    return search_request


# Search for products with filter
def search():
    # [TRY DIFFERENT FILTER EXPRESSIONS HERE:]
    filter = '(colorFamily: ANY("black"))'

    search_request = get_search_request("Nest_Maxi", filter)
    search_response = get_search_service_client().search(search_request)
    print("---filtered search response---")
    print(search_response)


search()
