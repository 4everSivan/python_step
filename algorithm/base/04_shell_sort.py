"""
希尔排序：
 时间复杂度：O(n log n)
 空间复杂度：O(1)
 性质：ln-place 不稳定
"""
from tools import generate_random_list


def sort_method(lst: list) -> list:
    h = int(len(lst) / 2)
    for i in range(h, 0, -1):
        gap = i
        for j in range(0, len(lst) - gap):
            if lst[j] > lst[j + gap]:
                tmp = lst[j]
                lst[j] = lst[j + gap]
                lst[j + gap] = tmp
    return lst


if __name__ == '__main__':
    test_list = generate_random_list(30, 1, 1000)
    print("测试用例：{0}".format(test_list))
    print("排序结果：{0}".format(sort_method(test_list)))
