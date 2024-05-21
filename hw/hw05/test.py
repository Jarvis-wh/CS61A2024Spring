from hw05 import hailstone
from hw05 import tree

t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
print(t1)