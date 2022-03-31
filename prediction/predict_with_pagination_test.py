import re
import subprocess

from predict_with_pagination import predict


def test_predict_with_pagination_pass():
    output = str(
        subprocess.check_output(
            "python predict_with_pagination.py", shell=True
        )
    )

    assert re.match(".*predict request.*", output)
    assert re.match(".*predict response.*", output)
    # check the response contains some movies
    assert re.match(".*results.*id.*", output)


def test_predict_with_pagination_response():
    response = predict()

    assert len(response.results) == 5
