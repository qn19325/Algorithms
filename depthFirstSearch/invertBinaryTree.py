class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def invert_tree(root: Node) -> Node:
        if not root:
            return root
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp 
        dfs(root)
        return root
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
    res = invert_tree(root)
    def dfs(root):
        if not root:
            return None
        print(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(res)