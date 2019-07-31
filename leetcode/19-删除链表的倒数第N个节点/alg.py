# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        for i in range(n):
            fast = fast.next

        if fast is None:  # 说明要删除的节点是第一个节点
            return head.next


        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


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
    lst = [1, 2, 3, 4, 5]
    head = buildList(lst)

    solution = Solution()
    head = solution.removeNthFromEnd(head, 3)
    scanList(head)
