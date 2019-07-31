# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        guard = ListNode(-1)  # 哨兵节点
        guard.next = head
        start = guard

        p1 = guard
        p2 = head
        p3 = head.next

        while start.next is not None:
            p2.next = p3.next
            p3.next = p2
            p1.next = p3

            if start.next.next.next is not None and start.next.next.next.next is not None:  # 确保移动之后p1和p2不是None
                p1 = start.next.next
                p2 = p1.next
                p3 = p2.next
                start = start.next.next  # 转移两步
            else:
                break
        return guard.next


def buildList(lst):
    tmp = None
    head = None
    for l in lst:
        if head is None:
            head = ListNode(l)
            tmp = head
        else:
            tmp.next = ListNode(l)
            tmp = tmp.next
    return head


def scanList(head):
    results = []
    while head is not None:
        results.append(str(head.val))
        head = head.next
    print('>'.join(results))


if __name__ == '__main__':
    head = buildList([1, 2, 3, 4, 5])

    solution = Solution()

    res = solution.swapPairs(head)
    scanList(res)
