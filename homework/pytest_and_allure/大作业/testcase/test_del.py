import pytest


class Test_del():
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("name", ['haizhenyu', 'xueqin'])
    def test_normal_del(self, objectget, name):
        try:
            results = objectget.delete_hero(name)
            assert results is not False
        except AssertionError:
            raise
        else:
            try:
                for i in results:
                    assert i.get(name) is None
            except AssertionError:
                raise
