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


import time

from google.api_core.client_options import ClientOptions
from google.api_core.operations_v1.operations_client import OperationsClient
from google.cloud.retail import BigQuerySource, ProductInputConfig, ProductServiceClient, \
    ImportProductsRequest

# TODO Define the project number and project Id here:
project_number = ""
project_id = ""

endpoint = "test-retail.sandbox.googleapis.com:443"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/1".format(project_number)
dataset_id = "products"
table_id = "products_for_import"
# TO CHECK ERROR HANDLING USE THE TABLE OF INVALID PRODUCTS
#table_id = "products_for_import_some_invalid"

# [START product_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END product_client]


# [START operation_client]
def get_operation_service_client():
    return OperationsClient
    # [END operation_client]


# [START get_import_products_big_query_request]
def get_import_products_big_query_request(reconciliation_mode):
    # TO CHECK ERROR HANDLING PASTE THE INVALID CATALOG NAME HERE:
    # default_catalog = "invalid_catalog"
    big_query_source = BigQuerySource()
    big_query_source.project_id = project_id
    big_query_source.dataset_id = dataset_id
    big_query_source.table_id = table_id
    big_query_source.data_schema = "product"

    input_config = ProductInputConfig()
    input_config.big_query_source = big_query_source

    import_request = ImportProductsRequest()
    import_request.parent = default_catalog
    import_request.reconciliation_mode = reconciliation_mode
    import_request.input_config = input_config

    print("---import products from big query table request---")
    print(import_request)

    return import_request
    # [END get_import_products_big_query_request]


# [START import_products_from_big_query]
def import_products_from_big_query():
    # TRY THE FULL RECONCILIATION MODE HERE:
    reconciliation_mode = ImportProductsRequest.ReconciliationMode.INCREMENTAL

    import_big_query_request = get_import_products_big_query_request(reconciliation_mode)
    big_query_operation = get_product_service_client().import_products(import_big_query_request)

    print(big_query_operation.operation.name)

    operation_status = get_operation_service_client().get_operation(big_query_operation.operation.name)

    while not operation_status:
        print("---please wait till operation is done---")
        time.sleep(5)

    print("---import products operation is done---")
    # [END import_products_from_big_query]


import_products_from_big_query()
