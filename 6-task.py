class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    stack = []
    ans = []
    cur = root

    while cur != None or len(stack) > 0:
        while cur != None:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right

    return ans