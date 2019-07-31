# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        tmp = head
        stack = [None] * k
        top = -1
        for _ in range(k):  # 确保存在k个可以交换的位置
            if tmp is None:
                return head
            top += 1
            stack[top] = tmp
            tmp = tmp.next

        next_part = stack[top].next
        now_head = stack[top]

        while top > 0:
            stack[top].next = stack[top - 1]
            top -= 1
        stack[top].next = self.reverseKGroup(next_part, k)

        return now_head


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
    head = buildList([1, 2, 3, 4])

    solution = Solution()

    now_head = solution.reverseKGroup(head, 2)

    scanList(now_head)
