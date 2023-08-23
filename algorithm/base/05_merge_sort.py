"""
归并排序：
 时间复杂度：O(n log n)
 空间复杂度：O(1)
 性质：ln-place 不稳定
"""
from tools import generate_random_list


def merge_sort(lst: list, tmp_lst: list, left: int, mid: int, right: int):
    l_pot = left
    r_pot = mid + 1
    t_pot = left

    # merge
    while l_pot <= mid and r_pot <= right:
        if lst[l_pot] < lst[r_pot]:
            tmp_lst[t_pot] = lst[l_pot]
            l_pot += 1
        else:
            tmp_lst[t_pot] = lst[r_pot]
            r_pot += 1
        t_pot += 1

    # merge left
    while l_pot <= mid:
        tmp_lst[t_pot] = lst[l_pot]
        t_pot += 1
        l_pot += 1

    # merge right
    while r_pot <= right:
        tmp_lst[t_pot] = lst[r_pot]
        t_pot += 1
        r_pot += 1

    # copy
    while left <= right:
        lst[left] = tmp_lst[left]
        left += 1


def merge_list(lst: list, tmp_lst: list, left: int, right: int):
    if left < right:
        mid = int((left + right) / 2)
        # recursion left
        merge_list(lst, tmp_lst, left, mid)
        # recursion right
        merge_list(lst, tmp_lst, mid + 1, right)
        # while list length is 1
        merge_sort(lst, tmp_lst, left, mid, right)


def sort_method(lst: list) -> list:
    length = len(lst)
    merge_list(lst, [None] * length, 0, length - 1)
    return lst


if __name__ == '__main__':
    test_list = generate_random_list(30, 1, 100)
    print("测试用例：{0}".format(test_list))
    print("排序结果：{0}".format(sort_method(test_list)))