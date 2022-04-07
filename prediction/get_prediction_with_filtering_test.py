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
#
import re
import subprocess

from get_prediction_with_filtering import predict


def test_get_prediction_with_filtering_pass():
    output = str(
        subprocess.check_output(
            "python get_prediction_with_filtering.py", shell=True
        )
    )

    assert re.match(".*predict request.*", output)
    assert re.match(".*predict response.*", output)
    # check the response contains some movies
    assert re.match(".*results.*id.*", output)


def test_get_prediction_with_filtering_response():
    response = predict()

    assert len(response.results) == 20
    # assert not re.search(".*OUT_OF_STOCK.*", str(response.results))
    # assert re.search(".*premium.*", str(response.results[0]))
