from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""


# Get search service client
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)


# Get Search Request with Boost specification
def get_search_request(query: str, _condition: str, _boost_strength: float):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    boost_spec = SearchRequest().BoostSpec()
    boost_spec.ConditionBoostSpec().condition = _condition
    boost_spec.ConditionBoostSpec.boost = _boost_strength

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.visitor_id = "123456"  # A unique identifier for tracking visitors
    search_request.boost_spec = boost_spec

    print("---search request---")
    print(search_request)

    return search_request


# [END search_product_with_boost_spec]

def search():
    # TRY DIFFERENT BOOST CONDITIONS HERE:
    condition = '(colorFamily: ANY("blue"))'
    boost = 0.5

    search_request = get_search_request("Nest_Maxi", condition, boost)
    search_response = get_search_service_client().search(search_request)
    print("---boost search response---")
    print(search_response)


search()
