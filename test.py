from binarytree import *
from treap import *
from avl import *

Tree = BinaryTree
#Tree = Treap
#Tree = AVLTree

def main():
    import random
    print 'tree:', Tree.name
    k = 15
    for n in [2**i for i in range(k, k+1)]:
        bt = Tree()
        l = []
        for _ in range(n):
            x = random.randrange(1000000000)
            if not bt.insert(x):
                if 0:print _, 'duplicate'
            l.append(x)
        print n, bt.depth()
        #assert bt.to_list() == list(sorted(set(l)))


if __name__ == '__main__':
    main()
