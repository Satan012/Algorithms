def setChild(root, left, right):
    root.left = left
    root.right = right


def reverse_walk(root, val=0):
    val_r = 0
    val_l = 0
    if root.right is not None:
        val_r = reverse_walk(root.right, val)
    if root.left is not None:
        val_l = reverse_walk(root.left, root.val + max([val_r, val]))

    root.val += max([val_r, val])  # 只能加右边的

    return max([val_l, root.val])  # 返回最大的


def check(root):
    if root.right is not None:
        check(root.right)
    print(root.val)
    if root.left is not None:
        check(root.left)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode):
        return reverse_walk(root, 0)


if __name__ == '__main__':
    # r4 = TreeNode(4)
    # r1 = TreeNode(1)
    # r6 = TreeNode(6)
    # r0 = TreeNode(0)
    # r2 = TreeNode(2)
    # r5 = TreeNode(5)
    # r7 = TreeNode(7)
    # r3 = TreeNode(3)
    # r8 = TreeNode(8)
    #
    # setChild(r4, r1, r6)
    # setChild(r1, r0, r2)
    # setChild(r6, r5, r7)
    # setChild(r2, None, r3)
    # setChild(r7, None, r8)

    r0 = TreeNode(0)
    r1 = TreeNode(1)
    r2 = TreeNode(2)
    r3 = TreeNode(3)

    setChild(r1, r0, r2)
    setChild(r2, None, r3)

    check(r1)

    solve = Solution()
    solve.bstToGst(r1)
    print('---------------')
    check(r1)
