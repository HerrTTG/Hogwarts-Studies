import pytest
import requests


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
class Test_serch:
    def test_search_pet(self, envget, status):
        search_usr = envget + "/findByStatus"
        params = {
            "status": status
        }
        # 发出查询请求
        r = requests.get(search_usr, params=params)
        # 状态断言
        assert r.status_code == 200
        # 业务断言
        assert r.json() != []
