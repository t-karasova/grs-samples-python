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

# [START add_remove_fulfillment_places]
import datetime
import os
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail import ProductServiceClient, AddFulfillmentPlacesRequest, RemoveFulfillmentPlacesRequest

from setup_cleanup import create_product, get_product, delete_product

project_number = os.getenv('PROJECT_NUMBER')
endpoint = "retail.googleapis.com"
product_id = "fulfillment_test_product_id"
product_name = 'projects/' + project_number + '/locations/global/catalogs/default_catalog/branches/default_branch/products/' + product_id

# The request timestamp
request_time = datetime.datetime.now()
# The outdated request timestamp
# request_time = datetime.datetime.now() - datetime.timedelta(days=1)


# get product service client
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)


# add fulfillment request
def get_add_fulfillment_request(product_name: str) -> AddFulfillmentPlacesRequest:
    add_fulfillment_request = AddFulfillmentPlacesRequest()
    add_fulfillment_request.product = product_name
    add_fulfillment_request.type_ = 'pickup-in-store'
    add_fulfillment_request.place_ids = ['store1', 'store2', 'store3']
    add_fulfillment_request.add_time = request_time
    add_fulfillment_request.allow_missing = True

    print("---add fulfillment request---")
    print(add_fulfillment_request)

    return add_fulfillment_request


# add fulfillment places to product
def add_fulfillment_places(product_name: str):
    add_fulfillment_request = get_add_fulfillment_request(product_name)
    get_product_service_client().add_fulfillment_places(add_fulfillment_request)
    print("---add fulfillment places, wait 10 seconds :---")
    time.sleep(10)


# remove fulfillment request
def get_remove_fulfillment_request(product_name: str) -> RemoveFulfillmentPlacesRequest:
    remove_fulfillment_request = RemoveFulfillmentPlacesRequest()
    remove_fulfillment_request.product = product_name
    remove_fulfillment_request.type_ = 'pickup-in-store'
    remove_fulfillment_request.place_ids = ['store1']
    remove_fulfillment_request.remove_time = request_time
    remove_fulfillment_request.allow_missing = True

    print("---remove fulfillment request---")
    print(remove_fulfillment_request)

    return remove_fulfillment_request


# remove fulfillment places to product
def remove_fulfillment_places(product_name: str):
    remove_fulfillment_request = get_remove_fulfillment_request(product_name)
    get_product_service_client().remove_fulfillment_places(remove_fulfillment_request)
    print("---remove fulfillment places, wait 10 seconds:---")
    time.sleep(10)

# [END add_remove_fulfillment_places]


create_product(product_id)
add_fulfillment_places(product_name)
#remove_fulfillment_places(product_name)
get_product(product_name)
#delete_product(product_name)
