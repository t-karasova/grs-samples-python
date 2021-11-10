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
from google.cloud.retail import SearchServiceClient, SearchRequest

# TODO Define the project number here:
project_number = ""
default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"


# [START get_search_service_client
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)
    # [END get_search_service_client


# [START search_with_filter]
def search():
    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    # CHANGE THE QUERY HERE:
    search_request.query = "sweater"
    search_request.filter = '(attributes.ecofriendly: ANY("recycled packaging"))'
    search_request.page_size = 10
    search_request.visitor_id = "123456"  # A unique identifier to track visitors

    print("---search_request:---")
    print(search_request)

    search_response = get_search_service_client().search(search_request)
    print("---search response---")
    print(search_response)
    # [END search_with_filter]


search()