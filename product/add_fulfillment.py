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

import datetime
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail import ProductServiceClient, AddFulfillmentPlacesRequest
from google.protobuf.timestamp_pb2 import Timestamp
from setup_cleanup import create_product

# TODO Define the project number here:
project_number = "945579214386"
endpoint = "retail.googleapis.com"
product_name = 'projects/' + project_number + '/locations/global/catalogs/default_catalog/branches/default_branch/products/test_product_id'

# [START get_product_service_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END get_product_service_client]


# [START add_fulfillment_request]
def get_add_fulfillment_request(product_name: str) -> object:
    add_fulfillment_request = AddFulfillmentPlacesRequest()
    add_fulfillment_request.product = product_name
    add_fulfillment_request.type_ = 'pickup-in-store'
    add_fulfillment_request.place_ids = ['store1', 'store2', 'store3']
    add_fulfillment_request.add_time = datetime.datetime.now()
    add_fulfillment_request.allow_missing = True

    print("---get product request---")
    print(add_fulfillment_request)

    return add_fulfillment_request
    # [END get_product_request]


# [START add_fulfillment]
def add_fulfillment_places(product_name: str):

    add_fulfillment_request = get_add_fulfillment_request(product_name)
    operation = get_product_service_client().add_fulfillment_places(add_fulfillment_request)

    print("---AddFulfillmentPlacements operation started:---")
    print(operation.operation.name)

    while not operation.done():
        print("---please wait till operation is done---")
        time.sleep(3)

add_fulfillment_places(product_name)

#create_product(product_name)