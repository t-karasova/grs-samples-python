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

import subprocess
import shlex
import time
import re


def get_project_id():
    get_project_command = "gcloud config get-value project --format json"
    config = subprocess.check_output(shlex.split(get_project_command))
    project_id = re.search('\"(.*?)\"', str(config)).group(1)
    print(project_id)
    return project_id


def create_gcs_bucket():
    create_gcs_bucket_command = "gsutil mb gs://{}".format(get_project_id())
    create_bucket_output = subprocess.check_output(shlex.split(create_gcs_bucket_command))
    print(create_bucket_output)


def upload_data_to_gcs_bucket(file_name):
    upload_files_gcs_command = "gsutil cp {} gs://{}".format(file_name, get_project_id())
    create_bucket_output = subprocess.check_output(shlex.split(upload_files_gcs_command))
    print(create_bucket_output)


get_project_id()
create_gcs_bucket()
time.sleep(5)
upload_data_to_gcs_bucket("/Users/Tatiana/GRS/repositories_code_samples/grs-samples-python/search/products_for_search.json")
time.sleep(5)