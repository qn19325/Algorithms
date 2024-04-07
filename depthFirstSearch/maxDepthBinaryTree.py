class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def max_depth(root: Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return 1 + max(dfs(root.left), dfs(root.right))
    return dfs(root)
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
    res = max_depth(root)
    print(res)
