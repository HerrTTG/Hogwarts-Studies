def bubble_sort(arr):
    """
    中间是你要实现的代码
    冒泡排序
    输入是一个数组
    降序
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):  # j为列表下标
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([1, 2, 3]))
