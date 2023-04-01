import unittest
import requests

HOST = "http://127.0.0.1:6000"

class TestApi(unittest.TestCase):

    def test_sub_endpoint(this):
        response = requests.get(f"{HOST}/api/sub", params={
            "lhs": 10,
            "rhs": 2
        })
        assert response.status_code == 200
        assert response.json().get("result") == 8

    def test_multipy_endpoint(this):
        response = requests.get(f"{HOST}/api/multiply", params={
            "lhs": 5,
            "rhs": 5
        })
        assert response.status_code == 200
        assert response.json().get("result") == 25

    def test_divide_endpoint(this):
        response = requests.get(f"{HOST}/api/divide", params={
            "lhs": 10,
            "rhs": 2
        })
        assert response.status_code == 200
        assert response.json().get("result") == 5

    def test_divide_endpoint_divisor_is_zero(this):
        response = requests.get(f"{HOST}/api/divide", params={
            "lhs": 10,
            "rhs": 0
        })
        assert response.status_code == 400
        assert response.json().get("error") == "Denominator can't be equal to 0"

    def test_sub_endpoint_invalid_input(this):
        response = requests.get(f"{HOST}/api/sub", params={
            "lhs": "a",
            "rhs": "b"
        })
        assert response.status_code == 400
        assert response.json().get("error") == "could not convert string to float: \'a\'"

    def test_sub_endpoint_with_no_parameters(this):
        response = requests.get(F"{HOST}/api/sub")
        assert response.status_code == 400
        assert response.json().get("error") == "Provide 'lhs' and 'rhs' parameters in request"