import pytest

@pytest.fixture(scope="session", autouse=True)
def project_start():
    print("\n🚀 接口自动化项目启动")
    yield
    print("\n🏁 自动化测试执行完成")