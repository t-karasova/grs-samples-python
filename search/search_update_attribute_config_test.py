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

# [START retail_search_for_products_with_query_parameter]
# Call Retail API to search for a products in a catalog using only search query.
#
import re

from search_attribute_config import search
from update_attribute_configuration import update_product

product_id = "GGOEAAEC172013"


def test_update_attribute_config():
    product = update_product(product_id)

    assert product.id == product_id
    assert 'ecofriendly' in product.attributes.keys()


def test_search_attribute_config():
    response = search()

    product_title = response.results[0].product.title
    assert re.match('.*Sweater.*', product_title)
    assert 'ecofriendly' in response.results[0].product.attributes.keys()
    assert response.total_size == 1
