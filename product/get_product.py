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

import random
import string

from google.api_core.client_options import ClientOptions
from google.cloud.retail import ProductServiceClient, GetProductRequest

from setup_cleanup import create_product, delete_product

# TODO Define the project number here:

project_number = ""
endpoint = "retail.googleapis.com"
product_id = ''.join(random.sample(string.ascii_lowercase, 8))


# [START get_product_service_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END get_product_service_client]


# [START get_product_request]
def get_product_request(product_name: str) -> object:
    get_product_request = GetProductRequest()
    get_product_request.name = product_name

    print("---get product request---")
    print(get_product_request)

    return get_product_request
    # [END get_product_request]


# [START get_product]
def get_product(product_name: str):
    # get a product from catalog
    get_request = get_product_request(product_name)
    get_product_response = get_product_service_client().get_product(get_request)

    print("---get product response:---")
    print(get_product_response)
    return get_product_response
    # [END get_product]


# create a product
created_product = create_product(product_id)
# GET CREATED PRODUCT
product = get_product(created_product.name)
# remove created product
delete_product(created_product.name)
