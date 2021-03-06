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

# [START add_fulfillment_places]
import datetime
import os
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail import FulfillmentInfo, PriceInfo, \
    ProductServiceClient, SetInventoryRequest
from google.cloud.retail_v2 import Product
from google.protobuf.field_mask_pb2 import FieldMask

from setup.setup_cleanup import create_product, delete_product, get_product

project_number = os.getenv('PROJECT_NUMBER')
endpoint = "retail.googleapis.com"
product_id = "inventory_test_product_id"
product_name = 'projects/' + project_number + '/locations/global/catalogs/default_catalog/branches/default_branch/products/' + product_id


# get product service client
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)


# product inventory info
def get_product_with_inventory_info(product_name: str) -> Product:
    price_info = PriceInfo()
    price_info.price = 15.0
    price_info.original_price = 20.0
    price_info.cost = 8.0
    price_info.currency_code = "USD"

    fulfillment_info = FulfillmentInfo()
    fulfillment_info.type_ = "pickup-in-store"
    fulfillment_info.place_ids = ["store1", "store2"]

    product = Product()
    product.name = product_name
    product.price_info = price_info
    product.fulfillment_info = [fulfillment_info]
    product.availability = "IN_STOCK"

    return product


# set inventory request
def get_set_inventory_request(product_name: str) -> SetInventoryRequest:
    # The request timestamp
    request_time = datetime.datetime.now()
    # The out-of-order request timestamp
    # request_time = datetime.datetime.now() - datetime.timedelta(days=1)
    set_mask = FieldMask(
        paths=['price_info', 'availability', 'fulfillment_info',
               'available_quantity'])

    set_inventory_request = SetInventoryRequest()
    set_inventory_request.inventory = get_product_with_inventory_info(
        product_name)
    set_inventory_request.set_time = request_time
    set_inventory_request.allow_missing = True
    set_inventory_request.set_mask = set_mask

    print("---set inventory request---")
    print(set_inventory_request)

    return set_inventory_request


# set inventory to product
def set_inventory(product_name: str):
    set_inventory_request = get_set_inventory_request(product_name)
    get_product_service_client().set_inventory(set_inventory_request)

    # This is a long running operation and its result is not immediately present with get operations,
    # thus we simulate wait with sleep method.
    print("---set inventory, wait 30 seconds:---")
    time.sleep(50)


create_product(product_id)
set_inventory(product_name)
get_product(product_name)
delete_product(product_name)
# [END add_fulfillment_places]
