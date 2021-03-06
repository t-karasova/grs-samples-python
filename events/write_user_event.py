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


# [START retail_write_user_event]
# Import user events into a catalog from inline source using Retail API
#
import datetime
import os

from google.api_core.client_options import ClientOptions
from google.cloud.retail import UserEvent, UserEventServiceClient, \
    WriteUserEventRequest
from google.protobuf.timestamp_pb2 import Timestamp

from setup.setup_cleanup import purge_user_event

project_number = os.getenv('PROJECT_NUMBER')

endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog"\
    .format(project_number)
visitor_id = 'test_visitor_id'


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get user event
def get_user_event():
    timestamp = Timestamp()
    timestamp.seconds = int(datetime.datetime.now().timestamp())

    user_event = UserEvent()
    user_event.event_type = "home-page-view"
    user_event.visitor_id = visitor_id
    user_event.event_time = timestamp

    print(user_event)
    return user_event


# get write user event request
def get_write_event_request(user_event):
    # TO CHECK THE ERROR HANDLING TRY TO PASS INVALID CATALOG:
    # default_catalog = "projects/{0}/locations/global/catalogs/invalid_catalog"\
    # .format(project_number)
    write_user_event_request = WriteUserEventRequest()
    write_user_event_request.user_event = user_event
    write_user_event_request.parent = default_catalog

    print("---write user event request---")
    print(write_user_event_request)

    return write_user_event_request


# call the Retail API to write user event
def write_user_event():
    write_user_event_request = get_write_event_request(get_user_event())
    user_event = get_user_events_service_client().write_user_event(
        write_user_event_request)

    print("---written user event:---")
    print(user_event)
    return user_event


write_user_event()
purge_user_event(visitor_id)

# [END retail_write_user_event]
