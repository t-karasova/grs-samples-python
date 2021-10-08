import random
import random
import string
import time

from google.api_core.client_options import ClientOptions
from google.cloud.retail_v2 import SearchServiceClient, Product, PriceInfo, ColorInfo, \
    ProductServiceClient, CreateProductRequest, DeleteProductRequest, CustomAttribute, FulfillmentInfo
from google.protobuf.field_mask_pb2 import FieldMask

project_number = "SET HERE VALID PROJECT NUMBER"
endpoint = "retail.googleapis.com"
isolation_filter_key = "INTEGRATION_FILTER_KEY"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog/branches/0".format(project_number)
default_search_placement = "projects" + project_number + "locations/global/catalogs/default_catalog/placements/default_search"
created_products = []


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


def delete_ingested_products(products: [Product]):
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


def ingest_products(test__id: str):
    print("---ingesting products to catalog---")
    create_product_for_search(get_primary_products(), test__id)
    print("---wait for ingested products to be indexed in catalog---")
    time.sleep(10)


def delete_products():
    print("---removing ingested products---")
    delete_ingested_products(created_products)
    print("---products removed---")
