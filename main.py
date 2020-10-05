from tree import BinaryTree
from random import randint


arr = list(set([randint(0, 100) for i in range(20)]))
print("array length:", len(arr))

bst = BinaryTree(arr)
print("=====")

print("is balanced:", bst.is_balanced(bst.root))
print("tree height:", bst.get_height(bst.root))
print("=====")

bst.print_tree()
print("=====")

print(bst.get_sorted_array())
print(bst.get_sorted_array(reverse=True))
print("=====")

k = randint(1, len(arr))
print("k:", k)
print("expected min k elem:", bst.get_sorted_array()[k - 1])
print("actual:", bst.k_min_node(k, bst.root).value)
print("=====")

bst.balance(bst.root)
print("is balanced:", bst.is_balanced(bst.root))
print("tree height:", bst.get_height(bst.root))
print("=====")
