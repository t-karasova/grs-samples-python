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
from search_with_query_expansion_spec import search


def test_search_with_query_expansion_spec():
    response = search()

    assert len(response.results) == 10
    assert response.results[0].product.title == 'Google Youth Hero Tee Grey'
    assert response.results[2].product.title != 'Google Youth Hero Tee Grey'
    assert response.total_size == 34
    assert response.query_expansion_info.expanded_query == True
