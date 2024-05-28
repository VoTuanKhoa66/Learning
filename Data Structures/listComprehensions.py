squares = [x ** 2 for x in range(10)]

print(squares)

x = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(x)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
a = [num for elem in vec for num in elem]
# a = []
# for elem in vec:
#     for num in elem:
#         a.append(num)
print(a)

from math import pi
p = [str(round(pi, i)) for i in range(1,6)]
print(p)

