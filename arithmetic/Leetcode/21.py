# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class mytest(unittest.TestCase):
    def setUp(self):
        self.datas = [
            [list2listNode([1, 2, 4]), list2listNode(
                [1, 3, 4]), [1, 1, 2, 3, 4, 4]],
            [[], []]
        ]

    def test_case(self):
        for data in self.datas:
            l = myFunction(data[0], data[1])
            show_node(l)
            self.assertEqual(None, data[2])

def show_node(root:ListNode):
    while root:
        print(root.val)
        root = root.next

def list2listNode(l: list):
    root, per, cur = None, None, None
    for i in l:
        if per:
            cur = ListNode(i)
            per.next = cur
            per = cur
        else:
            per = ListNode(i)
        if not root:
            root = per
    return root


def myFunction(l1, l2):
    cur = l1
    while l2:
        if not cur.next:
            cur.next = l2
            return l1
        if cur.val <= l2.val:
            cur = cur.next
        else:
            temp = cur.next
            cur = l2
            cur.next = temp
            l2 = l2.next
    return l1


if __name__ == "__main__":
    unittest.main()
    # root = list2listNode([1, 2, 4])
    # print(root.val,root.next.val)
    # l = [1,3,2]
    # l.sort()
    # print(l)