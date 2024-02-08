import pytest


@pytest.mark.flaky(reruns=2, reruns_delay=2)
def testcase2(self):
    assert False
