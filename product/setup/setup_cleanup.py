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
import re
import shlex
import subprocess

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import NotFound
from google.cloud import storage
from google.cloud.retail_v2 import CreateProductRequest, DeleteProductRequest, \
    FulfillmentInfo, GetProductRequest, PriceInfo, Product, ProductServiceClient

project_number = os.getenv('PROJECT_NUMBER')
project_id = os.getenv('PROJECT_ID')
endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_number)
default_branch_name = "projects/" + project_number + "/locations/global/catalogs/default_catalog/branches/default_branch"


def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)


def generate_product() -> Product:
    price_info = PriceInfo()
    price_info.price = 30.0
    price_info.original_price = 35.5
    price_info.currency_code = "USD"
    fulfillment_info = FulfillmentInfo()
    fulfillment_info.type_ = "pickup-in-store"
    fulfillment_info.place_ids = ["store0", "store1"]
    return Product(
        title='Nest Mini',
        type_=Product.Type.PRIMARY,
        categories=['Speakers and displays'],
        brands=['Google'],
        price_info=price_info,
        fulfillment_info=[fulfillment_info],
        availability="IN_STOCK",
    )


def create_product(product_id: str) -> object:
    create_product_request = CreateProductRequest()
    create_product_request.product = generate_product()
    create_product_request.product_id = product_id
    create_product_request.parent = default_branch_name

    created_product = get_product_service_client().create_product(
        create_product_request)
    print("---product is created:---")
    print(created_product)

    return created_product


def delete_product(product_name: str):
    delete_product_request = DeleteProductRequest()
    delete_product_request.name = product_name
    get_product_service_client().delete_product(delete_product_request)

    print("---product " + product_name + " was deleted:---")


def get_product(product_name: str):
    get_product_request = GetProductRequest()
    get_product_request.name = product_name
    # product = get_product_service_client().get_product(get_product_request)
    #
    # print("---product:---")
    # print(product)
    try:
        product = get_product_service_client().get_product(get_product_request)
        print("---get product response:---")
        print(product)
        return product
    except NotFound as e:
        print(e.message)
        return e.message


def create_bucket(bucket_name: str):
    """Create a new bucket in Cloud Storage"""
    print("bucket name:" + bucket_name)
    buckets_in_your_project = str(list_buckets())
    if bucket_name in buckets_in_your_project:
        print("Bucket {} already exists".format(bucket_name))
    else:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = "STANDARD"
        new_bucket = storage_client.create_bucket(bucket, location="us")
        print(
            "Created bucket {} in {} with storage class {}".format(
                new_bucket.name, new_bucket.location, new_bucket.storage_class
            )
        )
        return new_bucket


def list_buckets():
    """Lists all buckets"""
    bucket_list = []
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        bucket_list.append(str(bucket))
        print(bucket.name)
    return bucket_list


def upload_blob(bucket_name, source_file_name):
    """Uploads a file to the bucket."""
    # The path to your file to upload
    # source_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    object_name = re.search('resources/(.*?)$', source_file_name).group(1)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, object_name
        )
    )


def create_bq_dataset(dataset_name):
    """Create a BigQuery dataset"""
    if dataset_name not in list_bq_datasets():
        create_dataset_command = 'bq --location=US mk -d --default_table_expiration 3600 --description "This is my dataset." {}:{}'.format(
            project_id, dataset_name)
        subprocess.check_output(shlex.split(create_dataset_command))
    else:
        print("dataset {} already exists".format(dataset_name))


def list_bq_datasets():
    """List BigQuery datasets in the project"""
    list_dataset_command = "bq ls --project_id {}".format(project_id)
    datasets = subprocess.check_output(shlex.split(list_dataset_command))
    print(datasets)
    return str(datasets)


def create_bq_table(dataset, table_name, schema):
    """Create a BigQuery table"""
    if table_name not in list_bq_tables(dataset):
        create_table_command = "bq mk --table {}:{}.{} {}".format(
            project_id,
            dataset,
            table_name, schema)
        output = subprocess.check_output(shlex.split(create_table_command))
        print(output)
    else:
        print("table {} already exists".format(table_name))


def list_bq_tables(dataset):
    """List BigQuery tables in the dataset"""
    list_tables_command = "bq ls {}:{}".format(project_id, dataset)
    tables = subprocess.check_output(shlex.split(list_tables_command))
    print("tables:")
    print(tables)
    return str(tables)


def upload_data_to_bq_table(dataset, table_name, source, schema):
    """Upload data to the table from specified source file"""
    upload_data_command = "bq load --source_format=NEWLINE_DELIMITED_JSON {}:{}.{} {} {}".format(
        project_id, dataset, table_name, source, schema)
    output = subprocess.check_output(shlex.split(upload_data_command))
    print(output)
