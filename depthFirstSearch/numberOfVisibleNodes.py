class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def visible_tree_node(root: Node) -> int:
    def dfs(root, max_so_far):
        if not root:
            return 0
        total = 0
        
        if root.val >= max_so_far:
            total += 1
           
        total += dfs(root.left, max(max_so_far, root.val))
        total += dfs(root.right, max(max_so_far, root.val))
        
        return total
    return dfs(root, -float('inf'))
##############################################################################
        

# this function builds a tree from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(['5', '4', '3', 'x', 'x', '8', 'x', 'x', '6', 'x', 'x']), int)
    res = visible_tree_node(root)
    print(res)
