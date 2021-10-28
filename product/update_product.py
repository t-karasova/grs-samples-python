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
from google.cloud.retail_v2 import Product, ProductServiceClient, UpdateProductRequest, PriceInfo
from google.cloud.retail_v2.types import product

from setup_cleanup import create_product, delete_product

# TODO Define the project number here:
project_number = " "

default_branch_name = "projects/" + project_number + "/locations/global/catalogs/default_catalog/branches/default_branch"
endpoint = "retail.googleapis.com:443"
generated_product_id = ''.join(random.sample(string.ascii_lowercase, 8))


# [START get_product_service_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END get_product_service_client]


# [START generate_product_for_update]
def generate_product_for_update(product_id: str) -> Product:
    price_info = PriceInfo()
    price_info.price = 20.0
    price_info.original_price = 25.5
    price_info.currency_code = "EUR"
    return product.Product(
        id=product_id,
        name='projects/' + project_number + '/locations/global/catalogs/default_catalog/branches/default_branch/products/' + product_id,
        title='Updated Nest Mini',
        type_=product.Product.Type.PRIMARY,
        categories=['Updated Speakers and displays'],
        brands=['Updated Google'],
        availability="OUT_OF_STOCK",
        price_info=price_info,
    )
    # [END generate_product_for_update]


# [START update_product_request]
def get_update_product_request(product_to_update: Product):
    update_product_request = UpdateProductRequest()
    update_product_request.product = product_to_update
    update_product_request.allow_missing = True
    # PASTE UPDATE MASK HERE:

    print("---update product request---")
    print(update_product_request)

    return update_product_request
    # [END update_product_request]


# [START update_product]
def update_product(original_product: Product):
    # update product
    updated_product = get_product_service_client().update_product(
        get_update_product_request(generate_product_for_update(original_product.id)))

    print('---updated product---:')
    print(updated_product)

    # [END update_product]


# create product
created_product = create_product(generated_product_id)
# UPDATE PRODUCT
update_product(created_product)
# delete product
delete_product(created_product.name)