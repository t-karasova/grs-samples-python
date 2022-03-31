import os

from google.cloud.retail_v2 import (
    PredictionServiceClient, UserEvent, ProductDetail,
    Product, PredictRequest
)
from google.api_core.client_options import ClientOptions


project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
placement_id = os.environ["GOOGLE_CLOUD_PLACEMENT"]
ENDPOINT = "retail.googleapis.com"


def get_predict_request(_params: dict):
    predict_placement = (
        f'projects/{project_id}/locations/global/catalogs/'
        f'default_catalog/placements/{placement_id}'
    )

    product = Product()
    product.id = "55106"
    product.title = "Design for Living (1933)"
    product.type_ = Product.Type.PRIMARY
    product.categories = ['Comedy|Romance']

    product_details = ProductDetail()
    product_details.product = product

    user_event = UserEvent()
    user_event.event_type = "detail-page-view"
    user_event.visitor_id = "1234"
    user_event.product_details = [product_details]

    predict_request = PredictRequest()
    predict_request.placement = predict_placement
    predict_request.user_event = user_event
    predict_request.params = _params

    print("---predict request---")
    print(predict_request)

    return predict_request


def predict():
    _params = {'returnProduct': True, 'diversityLevel': 'auto-diversity'}

    predict_client_options = ClientOptions(ENDPOINT)
    response = PredictionServiceClient(client_options=predict_client_options).predict(
        get_predict_request(_params)
    )

    print("---predict response---")
    print(response)

    return response


predict()
