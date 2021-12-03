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

from import_products_gcs import import_products_from_gcs
from setup_cleanup import get_product


def test_create_product():
    os.environ["BUCKET_NAME"] = "products"
    gcs_bucket = "gs://{}".format(os.getenv("BUCKET_NAME"))
    print(gcs_bucket)
    # The productId of an existent product in the GRS source
    product_id = 'GGCOGOAC101259'
    product_name = "projects/{}/locations/global/catalogs/default_catalog/branches/1/products/{}".format(
        os.getenv('PROJECT_NUMBER'), product_id)

    import_products_from_gcs()

    assert get_product(product_name).name == product_name
