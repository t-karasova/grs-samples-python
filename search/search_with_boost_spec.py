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


# [START get_search_service_client]
def get_search_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return SearchServiceClient(client_options=client_options)
    # [END get_search_service_client]


# [START get_search_request_with_boost_specification]
def get_search_request(query: str, condition: str, boost_strength: float):
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"

    condition_boost_spec = SearchRequest.BoostSpec.ConditionBoostSpec()
    condition_boost_spec.condition = condition
    condition_boost_spec.boost = boost_strength

    boost_spec = SearchRequest.BoostSpec()
    boost_spec.condition_boost_specs = [condition_boost_spec]

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.boost_spec = boost_spec

    print("---search request---")
    print(search_request)

    return search_request
    # [END get_search_request_with_boost_specification]


# [START search_product_with_boost_spec]
def search():
    # TRY DIFFERENT BOOST CONDITIONS HERE:
    condition = '(colorFamily: ANY("blue"))'
    boost = 1.0

    search_request = get_search_request("Tee", condition, boost)
    search_response = get_search_service_client().search(search_request)
    print("---boost search response---")
    print(search_response)
    # [END search_product_with_boost_spec]


search()
