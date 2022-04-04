import re
import subprocess

from predict_with_filter_tags import predict


def test_predict_with_filter_tags_pass():
    output = str(
        subprocess.check_output(
            "python predict_with_filter_tags.py", shell=True
        )
    )

    assert re.match(".*predict request.*", output)
    assert re.match(".*predict response.*", output)
    # check the response contains some movies
    assert re.match(".*results.*id.*", output)


def test_predict_with_filter_tags_response():
    response = predict()

    assert len(response.results) == 20
    item = str(response.results[0])
    assert re.search(".*(promotional|premium).*", item)
    assert not re.search(r"\"season sale\"", item)
