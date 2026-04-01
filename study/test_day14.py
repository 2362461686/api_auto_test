import requests

#接口的地址
url = "https://postman-echo.com/post"
# 单条接口测试用例
def test_single_order():
    data = {
        "order_id": "PY_SINGLE_001",
        "user_id": 1002,
        "product_name": "pytest测试商品",
        "amount": 299.99,
        "status": "CREATED"
    }
    res = requests.post(url, json=data)
    # 断言1：状态码为200
    assert res.status_code == 200
    res_json = res.json()
    # 断言2：订单号一致
    assert res_json["json"]["order_id"] == data["order_id"]
    # 断言3：金额一致
    assert res_json["json"]["amount"] == data["amount"]
    # 断言4：状态一致
    assert res_json["json"]["status"] == data["status"]

# 批量数据驱动测试用例（等价类+边界值）
def test_batch_orders():
    test_cases = [
        {"order_id": "PY_BATCH_001", "amount": 500, "status": "CREATED"},
        {"order_id": "PY_BATCH_002", "amount": 1000, "status": "CREATED"},
        {"order_id": "PY_BATCH_003", "amount": 1001, "status": "CREATED"},
        {"order_id": "PY_BATCH_004", "amount": 0.01, "status": "CREATED"},
        {"order_id": "PY_BATCH_005", "amount": -100, "status": "CREATED"},
    ]
    for case in test_cases:
        res = requests.post(url, json=case)
        assert res.status_code == 200
        res_json = res.json()
        assert res_json["json"]["order_id"] == case["order_id"]
        assert res_json["json"]["amount"] == case["amount"]