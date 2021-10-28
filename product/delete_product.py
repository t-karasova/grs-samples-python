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
from google.cloud.retail import ProductServiceClient, DeleteProductRequest

from setup_cleanup import create_product

# TODO Define the project number here:
project_number = " "
endpoint = "retail.googleapis.com:443"

default_branch_name = "projects/" + project_number \
                      + "/locations/global/catalogs/default_catalog/branches/default_branch"

product_id = ''.join(random.sample(string.ascii_lowercase, 8))


# [START get_product_service_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END get_product_service_client]


# [START get_delete_product_request]
def get_delete_product_request(product_name: str):
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name

    print("---delete product request---")
    print(delete_product_request)

    return delete_product_request
    # [END get_delete_product_request]


# [START delete_product]
def delete_product(product_name: str):
    delete_product_request = get_delete_product_request(product_name)
    get_product_service_client().delete_product(delete_product_request)

    print("deleting product " + product_name)
    print("---product was deleted:---")


# DELETE PRODUCT
delete_product(create_product(product_id).name)