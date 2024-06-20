class Array:
    def __init__(self, capacity) -> None:
        # 初始化数组时定义数组的容量
        self.n = capacity
        # 根据容量开辟空间
        self.data = [-1] * capacity
        # 记录当前元素量
        self.count = 0

    def insert(self, location, value):
        # count即有效容量和定义的数组容量一致表示数组已满。返回false
        if self.n == self.count:
            return False

        # 确保插入数据不在奇怪的位置上。
        # 如 假如现在已经有 x , y  ,z 三个元素，其位置为012，记录的当前元素量count为3，
        # 此时能插入的位置为0123.4是不可以插入的。最往后也只能插入3，即count=location
        # 原因是如果count<location，如插入位置4，则3这个位置就会空出，数组就不是线性得了。
        # 所以判断location也必须小于等于count
        if location < 0 or location > self.count:
            return False

        # self.count=location 则跳过循环
        # 否则从最后一位循环到要插入的位置location
        for i in range(self.count, location, -1):
            # 依次把元素向后移位
            self.data[i] = self.data[i - 1]

        self.data[location] = value
        self.count += 1
        return True

    def find(self, location):
        # 确保location不在奇怪的位置上。
        if location < 0 or location >= self.count:
            return -1

        return self.data[location]

    def delete(self, location):
        # 确保location不在奇怪的位置上。
        if location < 0 or location >= self.count:
            return False

        # 从删除位置后，开始循环。循环到当前结尾。
        for i in range(location + 1, self.count):
            # 依次把删除位置后的元素向前移位
            self.data[i - 1] = self.data[i]

        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功，容量超了
    assert not array.insert(0, 100)
    # 查询插入结果
    assert array.find(0) == 2
    assert array.find(1) == 3
    assert array.find(2) == 4
    assert array.find(3) == 1
    assert array.find(4) == 5

    # 超出位置或者尚未插入返回-1
    assert array.find(10) == -1

    # 判断当前容量为5
    assert array.count == 5

    assert array.delete(4)
    assert array.find(4) == -1
    assert not array.delete(10)
    # 直接修改
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()
