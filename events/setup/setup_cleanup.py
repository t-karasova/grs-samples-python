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


# [START retail_purge_user_event]
# Import user events into a catalog from inline source using Retail API
#
import datetime
import time
import os
from google.api_core.client_options import ClientOptions
from google.cloud.retail import UserEvent, UserEventServiceClient, \
    WriteUserEventRequest, PurgeUserEventsRequest, ProductDetail, Product
from google.protobuf.timestamp_pb2 import Timestamp


project_number = os.getenv('PROJECT_NUMBER')
endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(project_number)


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get user event
def get_user_event(visitor_id):
    timestamp = Timestamp()
    timestamp.seconds = int(datetime.datetime.now().timestamp())

    product = Product()
    product.id = 'test_id'

    product_detail = ProductDetail()
    product_detail.product = product
    product_detail.quantity = 3

    user_event = UserEvent()
    user_event.event_type = "detail-page-view"
    user_event.visitor_id = visitor_id
    user_event.event_time = timestamp
    user_event.product_details = [product_detail]

    print(user_event)
    return user_event


# write user event
def write_user_event(visitor_id):
    write_user_event_request = WriteUserEventRequest()
    write_user_event_request.user_event = get_user_event(visitor_id)
    write_user_event_request.parent = default_catalog
    user_event = get_user_events_service_client().write_user_event(write_user_event_request)
    print("---the user event is written---")
    print(user_event)
    return user_event


# purge user event
def purge_user_event(visitor_id):
    purge_user_event_request = PurgeUserEventsRequest()
    purge_user_event_request.filter = 'visitorId="{}"'.format(visitor_id)
    purge_user_event_request.parent = default_catalog
    purge_user_event_request.force = True
    purge_operation = get_user_events_service_client().purge_user_events(purge_user_event_request)

    print("---the purge operation was started:----")
    print(purge_operation.operation.name)
