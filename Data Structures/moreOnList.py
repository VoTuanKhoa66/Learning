fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
number = [1,2,3,4,5,6,7]

print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4

fruits.reverse()
print(f'fruits reversed : {fruits}')
fruits.append('grape')
print(f'append grape : {fruits}')
fruits.sort()
print(f'fruit sorted : {fruits}')
print(fruits.pop())