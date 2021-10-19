# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
    search_request.visitor_id = "123456"  # A unique identifier to track visitors

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
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.page_token = page_token

    print("---search_request:---")
    print(search_request)

    return search_request
    # [END get_search_request_for_the_next_page]


# [START search_for_products_with_pagination_next_page_token]
def search():
    search_request_first_page = get_search_request_first_page("Tee", 6)
    search_first_page_response = get_search_service_client().search(search_request_first_page)
    print("---next page token from the first page:---")
    print(search_first_page_response.next_page_token)

    next_page_token = search_first_page_response.next_page_token
    search_request_next_page = get_search_request_next_page("Tee", 6, next_page_token)
    search_response = get_search_service_client().search(search_request_next_page)

    print("---search results from the next page---")
    print(search_response)
    # [END search_for_products_with_pagination_next_page_token]


search()
