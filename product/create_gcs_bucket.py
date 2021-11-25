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

from setup_cleanup import get_project_id, create_bucket, list_buckets, upload_blob
#
get_project_id()
# create_gcs_bucket()
# upload_data_to_gcs_bucket("product/products.json")
# upload_data_to_gcs_bucket("product/products_some_invalid.json")
# get_buckets_list()

create_bucket()
upload_blob("product/products.json")
upload_blob("product/products_some_invalid.json")
list_buckets()