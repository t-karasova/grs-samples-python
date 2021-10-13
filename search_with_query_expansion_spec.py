from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""


# Get search service client
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# Get Search Request with query expansion specification
def get_search_request(query: str, condition: SearchRequest.QueryExpansionSpec.Condition):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    query_expansion_spec = SearchRequest().QueryExpansionSpec()
    query_expansion_spec.condition = condition

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors
    search_request.query_expansion_spec = query_expansion_spec

    print("---search_request:---")
    print(search_request)

    return search_request


# Search for products with query expansion specification
def search():
    # TRY DIFFERENT QUERY EXPANSION CONDITION HERE:
    condition = SearchRequest.QueryExpansionSpec.Condition.AUTO

    search_request = get_search_request("Nest_Maxi", condition)
    search_response = get_search_service_client().search(search_request)

    print("---query expansion search results---")
    print(search_response)


search()
