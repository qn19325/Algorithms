class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################################################     
def is_balanced(root: Node) -> bool:
    def dfs(root):
        if not root: 
            return [True, 0]

        left = dfs(root.left)
        right = dfs(root.right)

        isHeightOkay = abs(left[1] - right[1]) <= 1
        balanced = left[0] and right[0] and isHeightOkay

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
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
    res = is_balanced(root)
    print(res)
