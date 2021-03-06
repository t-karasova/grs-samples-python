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
import os

from google.api_core.client_options import ClientOptions
from google.cloud.retail import PurgeUserEventsRequest, UserEventServiceClient

from setup.setup_cleanup import write_user_event

project_number = os.getenv('PROJECT_NUMBER')

endpoint = "retail.googleapis.com"
default_catalog = "projects/{0}/locations/global/catalogs/default_catalog".format(
    project_number)


# get user events service client
def get_user_events_service_client():
    client_options = ClientOptions(endpoint)
    return UserEventServiceClient(client_options=client_options)


# get purge user event request
def get_purge_user_event_request():
    purge_user_event_request = PurgeUserEventsRequest()
    # TO CHECK ERROR HANDLING SET INVALID FILTER HERE:
    purge_user_event_request.filter = 'visitorId="test_visitor_id"'
    purge_user_event_request.parent = default_catalog
    purge_user_event_request.force = True
    print("---purge user events request---")
    print(purge_user_event_request)
    return purge_user_event_request


# call the Retail API to purge user event
def call_purge_user_events():
    purge_operation = get_user_events_service_client().purge_user_events(
        get_purge_user_event_request())

    print("---the purge operation was started:----")
    print(purge_operation.operation.name)


write_user_event("test_visitor_id")
call_purge_user_events()
# [END retail_purge_user_event]
