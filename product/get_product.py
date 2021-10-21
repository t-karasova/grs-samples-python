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
from google.cloud.retail_v2 import Product, ProductServiceClient, CreateProductRequest, GetProductRequest, DeleteProductRequest
from google.cloud.retail_v2.types import product

# TODO Define the project number here:
project_number = ""

default_branch_name = "projects/" + project_number + "/locations/global/catalogs/default_catalog/branches/default_branch"
endpoint = "retail.googleapis.com"

product_id = 'get-sample-product-id'


# [START get_product_service_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END get_product_service_client]


# [START generate_product_to_create]
def generate_product() -> Product:
    return product.Product(
        title='Nest Mini',
        type_=product.Product.Type.PRIMARY,
        categories=['Speakers and displays'],
        brands=['Google'],
        uri='http://www.test-uri.com',
    )
    # [END generate_product_to_create]


# [START create_product]
def create_product(product_to_create: Product, product_id: str) -> object:
    create_product_request = CreateProductRequest()
    create_product_request.product = product_to_create
    create_product_request.product_id = product_id
    create_product_request.parent = default_branch_name
    return get_product_service_client().create_product(create_product_request)
    # [END create_product]


# [START delete_created_product]
def delete_created_product(product_name: str):
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name
    return get_product_service_client().delete_product(delete_product_request)
    # [END delete_created_product]


# [START get_product_request]
def get_product_request(product_name: str) -> object:
    get_product_request = GetProductRequest()
    get_product_request.name = product_name

    print("---get product request---")
    print(get_product_request)

    return get_product_request
    # [END get_product_request]


# [START get_product]
def get_product_call():
    # create product
    created_product = create_product(generate_product(), product_id)
    # get product
    get_request = get_product_request(created_product.name)
    get_product_response = get_product_service_client().get_product(get_request)

    print("---get product response:---")
    print(get_product_response)
    # [END get_product]

    # delete product
    delete_created_product(created_product.name)
    print("---product was deleted:---")
