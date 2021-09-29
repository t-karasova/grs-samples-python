import random
import string
import time
import os

from google.api_core.client_options import ClientOptions
from google.protobuf.field_mask_pb2 import FieldMask

from google.cloud.retail_v2 import SearchServiceClient, SearchRequest, Product, PriceInfo, ColorInfo, \
    ProductServiceClient, CreateProductRequest, DeleteProductRequest, CustomAttribute, Interval, FulfillmentInfo

project_number = "1038874412926"
endpoint = "retail.googleapis.com"
isolation_filter_key = "INTEGRATION_FILTER_KEY"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/0".format(project_number)
default_search_placement = "projects/1038874412926/locations/global/catalogs/default_catalog/placements/default_search"


def get_search_service_client():
    client_options = ClientOptions(endpoint)
    return SearchServiceClient(client_options=client_options)


# [END search_client]

# [START ingesting products for search]
def get_product_service_client():
    client_options = ClientOptions(endpoint)
    return ProductServiceClient(client_options=client_options)


def get_primary_products():
    products = []
    product1 = Product()
    product2 = Product()

    price_info1 = PriceInfo()
    price_info1.price = 20.0
    price_info1.original_price = 25.0
    price_info1.cost = 10.0
    price_info1.currency_code = "USD"

    color_info1 = ColorInfo()
    color_info1.color_families = ["black"]
    color_info1.colors = ["carbon"]

    fulfillment_info1 = FulfillmentInfo()
    fulfillment_info1.type_ = "pickup-in-store"
    fulfillment_info1.place_ids = ["store1", "store2"]

    field_mask1 = FieldMask(paths=["title", "categories", "price_info", "color_info"])

    product1.title = "Nest_Maxi"
    product1.categories = ["Nest > speakers and displays"]
    product1.uri = "https://uri.com"
    product1.brands = ["Google"]
    product1.price_info = price_info1
    product1.color_info = color_info1
    product1.fulfillment_info = [fulfillment_info1]
    product1.retrievable_fields = field_mask1

    price_info2 = PriceInfo()
    price_info2.price = 15.0
    price_info2.original_price = 20.0
    price_info2.cost = 5.0
    price_info2.currency_code = "USD"

    color_info2 = ColorInfo()
    color_info2.color_families = ["blue"]
    color_info2.colors = ["sky"]

    fulfillment_info2 = FulfillmentInfo()
    fulfillment_info2.type_ = "pickup-in-store"
    fulfillment_info2.place_ids = ["store2", "store3"]

    field_mask2 = FieldMask(paths=["title", "categories", "price_info", "color_info"])

    product2.title = "Nest_Maxi"
    product2.categories = ["Nest > speakers and displays"]
    product2.uri = "https://uri.com"
    product2.brands = ["Google"]
    product2.price_info = price_info2
    product2.color_info = color_info2
    product2.fulfillment_info = [fulfillment_info2]
    product2.retrievable_fields = field_mask2

    products.append(product1)
    products.append(product2)
    return products


def get_variant():
    variant = Product()

    fulfillment_info = FulfillmentInfo()
    fulfillment_info.type_ = "ship-to-store"
    fulfillment_info.place_ids = ["store123"]

    variant.type_ = Product.Type.VARIANT
    variant.title = "Nest_Maxi_variant1"
    variant.uri = "https://uri.com"
    variant.fulfillment_info = [fulfillment_info]

    return variant


def create_product_for_search(products: [Product], test__id: str):
    created_products = []
    for product in products:
        attribute = CustomAttribute()
        attribute.text = test__id
        attribute.indexable = True
        isolation_filter = {isolation_filter_key: attribute}
        product.attributes = isolation_filter
        product_client = get_product_service_client()
        create_request = CreateProductRequest()
        create_request.product = product
        create_request.parent = default_catalog
        create_request.product_id = '{0}_{1}'.format(product.title, get_random_id())
        created_product = product_client.create_product(request=create_request)
        print(create_request)
        variant = get_variant()
        variant.primary_product_id = created_product.id
        create_request.product = variant
        create_request.product_id = '{0}_{1}'.format(variant.title, get_random_id())
        created_variant = product_client.create_product(request=create_request)
        print(create_request)
        created_products.append(created_product)
        created_products.append(created_variant)

    return created_products


def delete_products(products: [Product]):
    product_client = get_product_service_client()
    types = [Product.Type.VARIANT, Product.Type.PRIMARY]
    for _type in types:
        for product in products:
            if product.type_.__eq__(_type):
                delete_request = DeleteProductRequest()
                delete_request.name = product.name
                product_client.delete_product(request=delete_request)


def get_random_id():
    return ''.join(random.sample(string.ascii_lowercase, 10))


def build_isolation_filter(test__id: str):
    return 'attributes.{0}: ANY("{1}")'.format(isolation_filter_key, test__id)


# [END ingesting products for search]

# [START search_product]
def search_products(query: str):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product]

# [START search_product_with_filter]
def search_filtered_products(query: str, _filter: str, page_size=10):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = '{0} AND {1}'.format(build_isolation_filter(test_id), _filter)
    search_request.page_size = page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_filter]

# [START search_product_with_offset]
def search_products_with_offset(query: str, _offset: int, page_size=10):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.page_size = page_size
    search_request.offset = _offset
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_offset]

# [START search_product_with_page_size]
def search_products_with_page_size(query: str, _page_size: int):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.page_size = _page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_page_size]

# [START search_product_with_page_token]
def search_products_with_page_token(query: str, _page_size: int, _page_token: str):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.page_size = _page_size
    search_request.page_token = _page_token
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_page_token]

# [START search_product_with_boost_spec]
def search_products_with_boost_spec(query: str, _condition: str, _boost_strength: float):
    boost_spec = SearchRequest().BoostSpec()

    boost_spec.ConditionBoostSpec().condition = _condition
    boost_spec.ConditionBoostSpec.boost = _boost_strength

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.visitor_id = visitor_id
    search_request.boost_spec = boost_spec

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_boost_spec]

# [START search_product_with_boost_spec]
def search_products_with_query_expansion(query: str, _condition: SearchRequest.QueryExpansionSpec.Condition):
    query_expansion_spec = SearchRequest().QueryExpansionSpec()
    query_expansion_spec.condition = _condition

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.visitor_id = visitor_id
    search_request.query_expansion_spec = query_expansion_spec

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_boost_spec]

# [START search_product_with_order]
def search_ordered_products(query: str, order: str, page_size=10):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.order_by = order
    search_request.page_size = page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_order]

# [START search_product_with_textual_facet]
def search_products_textual_facet(query: str, key: str, page_size=10):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.facet_specs = [facet_spec]
    search_request.page_size = page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_textual_facet]

# [START search_product_with_numerical_facet]
def search_products_numerical_facet(query: str, key: str, intervals: [Interval], page_size=10):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_key.intervals = intervals
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.facet_specs = [facet_spec]
    search_request.page_size = page_size
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_numerical_facet]

# [START search_product_with_textual_facet_excluded_filter_keys]
def search_products_textual_facet_excluded_filter_keys(query: str, key: str, excluded_filter_keys: [str], _filter: str):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key
    facet_spec.excluded_filter_keys = excluded_filter_keys

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = '{0} AND {1}'.format(build_isolation_filter(test_id), _filter)
    search_request.facet_specs = [facet_spec]
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_textual_facet_excluded_filter_keys]

# [START search_product_with_textual_facet_restricted_values]
def search_products_textual_facet_restricted_values(query: str, key: str, restricted_values: [str]):
    facet_key = SearchRequest.FacetSpec().FacetKey()
    facet_key.key = key
    facet_key.restricted_values = restricted_values
    facet_spec = SearchRequest.FacetSpec()
    facet_spec.facet_key = facet_key

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.facet_specs = [facet_spec]
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_textual_facet_restricted_values]

# [START search_product_with_variant_rollup_keys]
def search_products_variant_rollup_keys(query: str, variant_rollup_keys: [str]):
    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.branch = default_catalog
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.variant_rollup_keys = variant_rollup_keys
    search_request.visitor_id = visitor_id

    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_textual_facet_restricted_values]

def test_call_search_methods():
    products_to_search_for = create_product_for_search(get_primary_products(), test_id)
    time.sleep(30)

    # [START testing different searches]
    search_response = search_products(title_query)
    print("SEARCH RESULTS")
    print(search_response.results)

    search_response = search_filtered_products(title_query, '(colorFamily: ANY("black"))')
    print("FILTERED SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_with_offset(title_query, 1)
    print("OFFSET SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_with_page_size(title_query, 1)
    print("PAGED SEARCH RESULTS")
    print(search_response.results)

    next_page_token = search_response.next_page_token
    search_response = search_products_with_page_token(title_query, 1, next_page_token)
    print("NEXT PAGE SEARCH RESULTS")
    print(search_response.results)

    search_response = search_ordered_products(title_query, "price desc")
    print("ORDERED SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_with_boost_spec(title_query, "(colorFamily: ANY(\"blue\"))", 0.5)
    print("BOOST SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_with_query_expansion(title_query,
                                                       SearchRequest.QueryExpansionSpec.Condition.AUTO)
    print("QUERY EXPANSION SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_textual_facet(title_query, "colorFamily")
    print("COLORFAMILY FACET")
    print(search_response.facets)
    print("TEXTUAL FACET SEARCH RESULTS")
    print(search_response.results)

    interval = Interval()
    interval.minimum = 10.0
    interval.exclusive_maximum = 20.0
    search_response = search_products_numerical_facet(title_query, "price", [interval])
    print("PRICE FACET")
    print(search_response.facets)
    print("NUMERICAL FACET SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_textual_facet_excluded_filter_keys(title_query, "colorFamily", ["colorFamily"],
                                                                     'colorFamily: ANY("black")')
    print("COLORFAMILY EXCLUDED FILTER FACET")
    print(search_response.facets)
    print("EXCLUDED FILTER KEY FACET SEARCH RESULT")
    print(search_response.results)

    search_response = search_products_textual_facet_restricted_values(title_query, "colorFamily", ["black"])
    print("COLORFAMILY RESTRICTED VALUE FACET")
    print(search_response.facets)
    print("RESTRICTED VALUE FACET SEARCH RESULTS")
    print(search_response.results)

    search_response = search_products_variant_rollup_keys(title_query, ["shipToStore.store123"])
    print("SEARCH RESULTS WITH VARIANT ROLLUP KEYS")
    print(search_response.results)

    # [END testing different searches]
    delete_products(products_to_search_for)
