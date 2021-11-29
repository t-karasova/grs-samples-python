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

from setup_cleanup import create_bq_dataset, create_bq_table, upload_data_to_bq_table

create_bq_dataset("products")
create_bq_table("products", "products")
upload_data_to_bq_table("products", "products", "product/products.json")
create_bq_table("products", "products_some_invalid")
upload_data_to_bq_table("products", "products_some_invalid", "product/products_some_invalid.json")
