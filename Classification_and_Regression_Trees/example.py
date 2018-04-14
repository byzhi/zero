from algorithm import *

# example 1
dataset = [[[1, 1], [1, 2]], [[1, 1], [1, 0]], [[1, 2], [1, 0]]]
class_values = [0, 1, 2]
"""
p:
0,1/2,1/2
1/2,1/2,0
1/2,0,1/2 

p*(1-p):
0,1/4,1/4
1/4,1/4,0
1/4,0,1/4

sum = 3/2
"""
print(gini(dataset, class_values))


# example 2
dataset = [[2.771244718, 1.784783929, 0],
           [1.728571309, 1.169761413, 0],
           [3.678319846, 2.81281357, 0],
           [3.961043357, 2.61995032, 0],
           [2.999208922, 2.209014212, 0],
           [7.497545867, 3.162953546, 1],
           [9.00220326, 3.339047188, 1],
           [7.444542326, 0.476683375, 1],
           [10.12493903, 3.234550982, 1],
           [6.642287351, 3.319983761, 1]]

s = split_dataset(dataset)
print('Split: [X%d < %.3f]' % ((s['index'] + 1), s['value']))

tree = tree_build(dataset, 2, 1)

tree_print(tree)