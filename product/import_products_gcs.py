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
from google.cloud.retail import GcsSource, ProductInputConfig, ProductServiceClient, ImportErrorsConfig, \
    ImportProductsRequest

# TODO Define the project number here:
project_number = ""

endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/1".format(project_number)
gcs_bucket = "gs://products_catalog/"
gcs_errors_bucket = "gs://products_catalog/error"
gcs_products_object = "products_for_search.json"


# [START product_client]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)
    # [END product_client]


# [START get_import_products_gcs_request]
def get_import_products_gcs_request(gcs_object_name: str):
    gcs_source = GcsSource()
    gcs_source.input_uris = ["{0}/{1}".format(gcs_bucket, gcs_object_name)]

    input_config = ProductInputConfig()
    input_config.gcs_source = gcs_source

    errors_config = ImportErrorsConfig()
    errors_config.gcs_prefix = gcs_errors_bucket

    import_request = ImportProductsRequest()
    import_request.parent = default_catalog
    import_request.reconciliation_mode = ImportProductsRequest.ReconciliationMode.INCREMENTAL
    import_request.input_config = input_config
    import_request.errors_config = errors_config

    print("---import products from google cloud source request---")
    print(import_request)

    return import_request
    # [END get_import_products_gcs_request]


# [START import_products_from_gcs]
def import_products_from_gcs():
    import_gcs_request = get_import_products_gcs_request(gcs_products_object)
    gcs_operation = get_product_service_client().import_products(import_gcs_request)

    print(gcs_operation.operation.name)

    while not gcs_operation.done():
        print("---please wait till operation is done---")
        time.sleep(5)

    print("---import products operation is done---")
    # [END import_products_from_gcs]


import_products_from_gcs()
