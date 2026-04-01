import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.http_client import HttpClient

url = "https://postman-echo.com/post"


# 参数化：5组等价类+边界值
@pytest.mark.parametrize("case_data", [
    {"order_id": "A001", "amount": 500, "status": "CREATED"},
    {"order_id": "A002", "amount": 1000, "status": "CREATED"},
    {"order_id": "A003", "amount": 1001, "status": "CREATED"},
    {"order_id": "A004", "amount": 0.01, "status": "CREATED"},
    {"order_id": "A005", "amount": -100, "status": "CREATED"},
])
def test_order_api(case_data):
    res = HttpClient.post(url, case_data)

    assert res.status_code == 200
    res_json = res.json()

    assert res_json["json"]["order_id"] == case_data["order_id"]
    assert res_json["json"]["amount"] == case_data["amount"]