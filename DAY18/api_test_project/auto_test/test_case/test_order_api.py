import sys
import os
import allure
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from common.http_client import HttpClient

url = "https://postman-echo.com/post"

# 正常场景 + 异常场景参数化
# 替换原来的 parametrize 部分
@pytest.mark.parametrize("case_data, expect_status, expect_error", [
    ({"order_id": "A001", "amount": 500, "status": "CREATED"}, 200, None),
    ({"order_id": "A002", "amount": 1000, "status": "CREATED"}, 200, None),
    ({"order_id": "A003", "amount": 0.01, "status": "CREATED"}, 200, None),
    ({"order_id": "A004", "amount": -100, "status": "CREATED"}, 200, None),
    ({"order_id": "", "amount": 500, "status": "CREATED"}, 200, None),
], ids=[
    "正常订单_500元",
    "正常订单_1000元",
    "边界值_0.01元",
    "异常场景_负数金额",
    "异常场景_空订单ID"
])
def test_order_api(case_data, expect_status, expect_error):
    # 给每个用例添加动态标题
    allure.dynamic.title(case_data["order_id"] if case_data["order_id"] else "空ID")
    allure.dynamic.description(f"测试金额: {case_data['amount']}")

    res = HttpClient.post(url, case_data)
    assert res.status_code == expect_status
    res_json = res.json()
    assert res_json["json"]["order_id"] == case_data["order_id"]
    assert res_json["json"]["amount"] == case_data["amount"]