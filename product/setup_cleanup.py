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

import os

from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import Product, ProductServiceClient, CreateProductRequest, DeleteProductRequest, PriceInfo
from google.cloud.retail_v2.types import product

project_number = os.getenv('PROJECT_NUMBER')

default_branch_name = "projects/" + project_number + "/locations/global/catalogs/default_catalog/branches/default_branch"
endpoint = "retail.googleapis.com:443"


def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)


def generate_product() -> Product:
    price_info = PriceInfo()
    price_info.price = 30.0
    price_info.original_price = 35.5
    price_info.currency_code = "USD"
    return product.Product(
        title='Nest Mini',
        type_=product.Product.Type.PRIMARY,
        categories=['Speakers and displays'],
        brands=['Google'],
        price_info=price_info,
        availability="IN_STOCK",
    )


def create_product(product_id: str) -> object:
    create_product_request = CreateProductRequest()
    create_product_request.product = generate_product()
    create_product_request.product_id = product_id
    create_product_request.parent = default_branch_name

    created_product = get_product_service_client().create_product(create_product_request)
    print("---product is created:---")
    print(created_product)

    return created_product


def delete_product(product_name: str):
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name
    get_product_service_client().delete_product(delete_product_request)

    print("---product " + product_name + "was deleted:---")
