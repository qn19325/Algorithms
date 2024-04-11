class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def binary_tree_paths(root: Node):
        paths = []
        def dfs(root, path):
            if not root:
                return

            if not root.right and not root.left:
                paths.append(path + str(root.val))
            
            dfs(root.left, path + str(root.val) + "->")
            dfs(root.right, path + str(root.val) + "->")
        dfs(root, "")
        return paths
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
    res = binary_tree_paths(root)
    print(res)