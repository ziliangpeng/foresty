
class Node:

    def __init__(self, val):
        self.val = val # make sure __lt__, __gt__ and __eq__ are implemented
        self.left = self.right = None


class BinaryTree:
    name = 'Naive Binary Tree'

    def __init__(self):
        self.root = None
        self.Node = Node

    def _insert(self, node, val):
        inserted = False
        if not node:
            node, inserted = self.Node(val), True
        elif val < node.val:
            node.left, inserted = self._insert(node.left, val)
        elif node.val < val:
            node.right, inserted = self._insert(node.right, val)
        return node, inserted

    def insert(self, val):
        self.root, inserted = self._insert(self.root, val)
        return inserted

    def _locate(self, node, val):
        if not node:
            return None
        elif val < node.val:
            return self._locate(node.left, val)
        elif node.val < val:
            return self._locate(node.right, val)
        else:
            return node

    def contains(self, val):
        return _locate(self.root, val) != None

    def _min(self, node):
        if node == None:
            return None
        else:
            return min(node.val, self._min(node.left))

    def _max(self, node):
        if node == None:
            return None
        else:
            return max(node.val, self._max(node.right))

    def _delete(self, node, val):
        if node == None:
            return None, False
        elif val < node.val:
            node.left, deleted = self._delete(node.left, val)
            return node, deleted
        elif node.val < val:
            node.right, deleted =  self._delete(node.right, val)
            return node, deleted
        else: # equals, deletes self
            if sorted(node.left, node.right)[0] == None: # one of the child is None
                return sorted(node.left, node.right)[1], True
            else: # both sons exist
                next_val = self._min(node.right)
                node.val = next_val
                node.right, _ = self._delete(node.right, next_val)
                return node, True

    def delete(self, val):
        return self._delete(self, self.root, val)[1]

    def _next_val(self, node, val): # wrong!
        if node is None:
            return None
        elif node.val <= val:
            return self._next_val(node.right, val)
        else:
            left_branch_result = self._next_val(node.left, val)
            if left_branch_result == None:
                return node.val
            else:
                return left_branch_result

    def _prev_val(self, node, val):
        if not node:
            return None
        elif node.val < val:
            right_branch_result = self._prev_val(node.right, val)
            if right_branch_result == None:
                return node.val
            else:
                return right_branch_result
        else:
            return self._prev_val(node.left, val)

    def next(self, val):
        return self._next_val(self.root, val)

    def prev(self, val):
        return self._prev_val(self.root, val)

    def _depth(self, node):
        if node is None:
            return 0
        return max(self._depth(node.left), self._depth(node.right)) + 1

    def depth(self):
        return self._depth(self.root)

    def _traverse(self, node):
        if node:
            for x in self._traverse(node.left):
                yield x
            yield node.val
            for x in self._traverse(node.right):
                yield x

    def to_list(self):
        return list(self._traverse(self.root))

    def __str__(self):
        return str(list(self._traverse(self.root)))


