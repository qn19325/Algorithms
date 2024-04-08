class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def has_path_sum(root: Node, targetSum: int) -> bool:
    if not root:
        return False

    def dfs(root, targetSum):
        if not root:
            return False
        targetSum = targetSum - root.val
        if not root.left and not root.right:
            return targetSum == 0
        return dfs(root.left, targetSum) or dfs(root.right, targetSum)

    return dfs(root, targetSum)
##############################################################################
        

# this function builds a tree from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(['3', '9', 'x', 'x', '20', '15', 'x', 'x', '7', 'x', 'x']), int)
    res = has_path_sum(root, 22)
    print(res)

