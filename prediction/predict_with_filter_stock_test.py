import re
import subprocess

from predict_with_filter_stock import predict


def test_predict_with_filter_tags_pass():
    output = str(
        subprocess.check_output(
            "python predict_with_filter_stock.py", shell=True
        )
    )

    assert re.match(".*predict request.*", output)
    assert re.match(".*predict response.*", output)
    # check the response contains some movies
    assert re.match(".*results.*id.*", output)


def test_predict_with_filter_tags_response():
    response = predict()

    assert len(response.results) == 20
    items = str(response.results)
    assert not re.search(".*OUT_OF_STOCK.*", items)

