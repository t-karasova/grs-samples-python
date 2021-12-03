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
import os
import re

from create_product import create_product
from setup_cleanup import delete_product, get_product


def test_create_product():
    generated_product_id = ''.join(random.sample(string.ascii_lowercase, 8))
    generated_product_name = "projects/{}/locations/global/catalogs/default_catalog/branches/0/products/{}".format(os.getenv('PROJECT_NUMBER'), generated_product_id)

    product = create_product(generated_product_id)

    assert product.name == generated_product_name
    delete_product(product.name)

    message = get_product(product.name)
    assert re.match(".*Product with name \"{}\" does not exist".format(generated_product_name), message)