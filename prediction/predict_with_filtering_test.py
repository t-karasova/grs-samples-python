import re
import subprocess

from predict_with_filtering import predict


def test_predict_with_filtering_pass():
    output = str(
        subprocess.check_output(
            "python predict_with_filtering.py", shell=True
        )
    )

    assert re.match(".*predict request.*", output)
    assert re.match(".*predict response.*", output)
    # check the response contains some movies
    assert re.match(".*results.*id.*", output)


def test_predict_with_filtering_response():
    response = predict()

    assert len(response.results) == 20
    assert not re.search(".*OUT_OF_STOCK.*", str(response.results))
    assert re.search(".*premium.*", str(response.results[0]))
