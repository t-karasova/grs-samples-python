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

import datetime
import os

from setup_cleanup import create_bucket, upload_blob

project_id = os.getenv('PROJECT_ID')

timestamp_ = datetime.datetime.now().timestamp().__round__()
bucket_name = "{}_{}".format(project_id, timestamp_)

create_bucket(bucket_name)
upload_blob(bucket_name, "resources/user_events.json")
upload_blob(bucket_name, "resources/user_events_some_invalid.json")

print("\nThe gcs bucket {} was created".format(bucket_name))
