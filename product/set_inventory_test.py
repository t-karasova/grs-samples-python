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
import pytest
import time

from set_inventory import set_inventory
from setup_cleanup import create_product, delete_product, get_product


@pytest.mark.flaky(reruns=5)
def test_add_fulfillment():
    generated_product_id = ''.join(random.sample(string.ascii_lowercase, 8))
    generated_product_name = "projects/{}/locations/global/catalogs/default_catalog/branches/0/products/{}".format(
        os.getenv('PROJECT_NUMBER'), generated_product_id)

    product = create_product(generated_product_id)

    set_inventory(product.name)
    #wait for the product inventory information updated to take effect to reduce the frequency of failure
    time.sleep(30)
    product_with_added_placements = get_product(product.name)

    assert product_with_added_placements.fulfillment_info[0].type_ == "pickup-in-store"
    assert sorted(product_with_added_placements.fulfillment_info[0].place_ids) == ['store1', 'store2']

    delete_product(product.name)

    message = get_product(product.name)
    assert re.match(".*Product with name \"{}\" does not exist".format(generated_product_name), message)

