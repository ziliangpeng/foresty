from binarytree import Node, BinaryTree
import utils

class Treap(BinaryTree):
    name = "Treap"
    from random import random as gen_prob

    class TreapNode(Node):

        def __init__(self, val):
            Node.__init__(self, val)
            self.prob = Treap.gen_prob()

    def __init__(self):
        BinaryTree.__init__(self)
        self.Node = self.TreapNode
        self._twist_cw = utils._twist_cw
        self._twist_ccw = utils._twist_ccw

    def _insert(self, node, val):
        inserted = False
        if not node:
            node, inserted = self.Node(val), True
        elif val < node.val:
            node.left, inserted = self._insert(node.left, val)
            if node.left.prob > node.prob:
                node = self._twist_cw(node)
        elif node.val < val:
            node.right, inserted = self._insert(node.right, val)
            if node.right.prob > node.prob:
                node = self._twist_ccw(node)
        return node, inserted
