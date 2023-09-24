# Part: 1. 链表
# Level: 青铜挑战
# Author: sivan
from typing import Optional, Union, List


__all__ = ['LinkedList']


class LinkedList(object):

    def __init__(self, val: Union[int, str], next_node: Optional['LinkedList'] = None) -> None:
        self.value = val
        self.next = next_node

    def insert(self, item: Union[int, str], position: int = None) -> None:
        """
        插入链表元素。
        :param item: 链表节点值。
        :param position:  插入位置，为空时默认插入链表尾端。
        :return: None
        """
        # insert tail
        if position is None or position > len(self) - 1:
            t_node = self
            while t_node.next is not None:
                t_node = t_node.next
            t_node.next = LinkedList(item)
        # insert head
        elif position <= 0:
            t_node = LinkedList(self.value, self.next)
            self.value = item
            self.next = t_node
        # insert middle
        else:
            p_node = self
            position -= 1
            while position - 1 >= 0:
                p_node = p_node.next
                position -= 1
            t_node = LinkedList(item)
            t_node.next = p_node.next
            p_node.next = t_node

    def delete(self, position: int) -> None:
        """
        删除链表指定元素。
        :param position: 链表节点值。
        :return: None
        """
        if position <= 0:
            t_node = self.next
            self.value = t_node.value
            self.next = t_node.next
        elif position > len(self) - 1:
            raise Exception("Error: LinkedList index out of bounds")
        elif position == len(self) - 1:
            p_node = self
            position -= 1
            while position - 1 >= 0:
                p_node = p_node.next
                position -= 1
            p_node.next = None
        else:
            p_node = self
            position -= 1
            while position - 1 >= 0:
                p_node = p_node.next
                position -= 1
            t_node = p_node.next
            p_node.next = t_node.next

    def to_list(self) -> List:
        """
        将链表转化为 List。
        :return: List
        """
        lst = []
        t_node = self
        while t_node is not None:
            lst.append(t_node.value)
            t_node = t_node.next
        return lst

    def __len__(self) -> int:
        count = 1
        t_node = self.next
        while t_node:
            count += 1
            t_node = t_node.next
        return count

    def __str__(self) -> str:
        return "LinkedList(value={}, next='{}')".format(self.value, self.next.value if self.next else None)


if __name__ == '__main__':
    link = LinkedList(1)
    link.insert(2)
    link.insert(3)
    link.insert(4)

    print(link.to_list())
