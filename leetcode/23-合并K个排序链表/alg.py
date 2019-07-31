# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 时间复杂度是O(Slogn), s是list最长的长度，n是list的数目
    def mergedTwo(self, lst1, lst2):
        p1 = lst1
        p2 = lst2
        res = ListNode(-1)
        res_rear = res
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                res_rear.next = p1
                p1 = p1.next
            else:
                res_rear.next = p2
                p2 = p2.next
            res_rear = res_rear.next

        p = p1 if p1 is not None else p2

        while p is not None:
            res_rear.next = p
            p = p.next
            res_rear = res_rear.next
        return res.next

    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        else:
            mid = length // 2
            leftResult = self.mergeKLists(lists[:mid])
            rightResult = self.mergeKLists(lists[mid:])
            return self.mergedTwo(leftResult, rightResult)


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
    head1 = buildList([1, 4, 5])
    head2 = buildList([1, 3, 4])
    head3 = buildList([2, 6])
    head4 = buildList([3, 5, 7, 8])

    solution = Solution()
    res = solution.mergeKLists([head1, head2, head3, head4])
    scanList(res)
    # res = solution.mergedTwo(head2, head3)
