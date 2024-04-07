class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def minDepth(root: Node) -> int:
    if not root: 
        return 0

    min_depth = 9999

    def dfs(node, cur_depth):
        if not node:
            return
        
        if not node.left and not node.right:
            nonlocal min_depth
            min_depth = min(min_depth, cur_depth + 1)

        dfs(node.left, cur_depth + 1)
        dfs(node.right, cur_depth + 1)

    dfs(root, 0)
    return min_depth
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
    res = minDepth(root)
    print(res)
