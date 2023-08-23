"""
冒泡排序：
 时间复杂度：O(n2)
 空间复杂度：O(1)
 性质：in-place 稳定
"""
from tools import generate_random_list


def sort_method(lst: list) -> list:
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] > lst[i]:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
    return lst


if __name__ == '__main__':
    test_list = generate_random_list(30, 1, 100)
    print("测试用例：{0}".format(test_list))
    print("排序结果：{0}".format(sort_method(test_list)))
