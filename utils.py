
def _twist_cw(node):
    left_child = node.left
    if left_child:
        node.left = left_child.right
        left_child.right = node
        node = left_child
    return node

def _twist_ccw(node):
    right_child = node.right
    if right_child:
        node.right = right_child.left
        right_child.left = node
        node = right_child
    return node
