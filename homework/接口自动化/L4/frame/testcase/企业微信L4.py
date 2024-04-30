import sys

sys.path.append('E:\霍格沃茨学社\Hogwarts-Studies\homework\接口自动化\L4')

from frame.apis.Address_book.department import Department


class Testcase():
    def inputenv(self, env):
        self.tester = Department(env)

    def test_case1(self, envget):
        self.inputenv(envget)
        self.tester.simplelist({'id': 1})
