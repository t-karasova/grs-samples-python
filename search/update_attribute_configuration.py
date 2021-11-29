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


# [START retail_update_attribute_config]
# Update product in a catalog using Retail API to change the product attribute searchability and indexability.
import os
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import ProductServiceClient, Product, UpdateProductRequest, GetProductRequest, \
    CustomAttribute

project_number = os.getenv('PROJECT_NUMBER')
product_id = "GGOEAAEC172013"


# get product service client
def get_product_service_client():
    client_options = ClientOptions("retail.googleapis.com")
    return ProductServiceClient(client_options=client_options)


def get_product(product_id):
    get_product_request = GetProductRequest()
    get_product_request.name = 'projects/' + project_number + '/locations/global/catalogs/default_catalog/branches/default_branch/products/' + product_id
    return get_product_service_client().get_product(get_product_request)


def get_update_product_request(product_to_update: Product):
    update_product_request = UpdateProductRequest()
    update_product_request.product = product_to_update

    print("---update product request---")
    print(update_product_request)
    return update_product_request


# update the product attribute
def update_product(product_to_update_id):
    # Get a product from catalog
    product_to_update = get_product(product_to_update_id)

    # Prepare the product attribute to be updated
    attribute = CustomAttribute()
    attribute.indexable = True
    attribute.searchable = False
    attribute.text = ["recycled fabrics",
                      "recycled packaging",
                      "plastic-free packaging",
                      "ethically made"]

    # Set the attribute to the original product
    product_to_update.attributes = {'ecofriendly': attribute}

    # Update product
    updated_product = get_product_service_client().update_product(
        get_update_product_request(product_to_update))

    print('---updated product---:')
    print(updated_product)

    print('---Wait 5 minutes to be sure the catalog has been indexed after the changes---:')
    time.sleep(60)
    print('---You can proceed with the search requests---')
    return updated_product


update_product(product_id)
# [END retail_update_attribute_config]