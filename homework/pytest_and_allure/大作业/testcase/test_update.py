import pytest


class Test_update():
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("name,volume", [['haizhenyu', 2], ['xueqin', 98]])
    def test_normal_update(self, objectget, name, volume):
        # 这里的volume是修改后的值
        try:
            result = objectget.update_hero(name, volume)
            assert result
        except AssertionError:
            raise
        else:
            try:
                assert result["name"] == name and result["volume"] == volume
            except AssertionError:
                raise
