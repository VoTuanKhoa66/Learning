print('doesn\'t' ) # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead

s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), special characters are interpreted, so \n produces new line

print('C:\\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

#One way is using triple-quotes: """...""" or '''...'''
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#Strings can be concatenated (glued together) with the + operator, and repeated with *
print(3 * 'un' + 'ium')

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py' 'thon') # but this only works with two literals though, not with variables or expressions If you want to concatenate variables or a variable and a literal, use +

#Strings can be indexed (subscripted), with the first character having index 0.
word = 'Python'
print(word[0])
print(word[-1]) # Note that since -0 is the same as 0, negative indices start from -1

#In addition to indexing, slicing is also supported.
print(word[0:2])

#out of range slice indexes are handled gracefully when used for slicing
print(word[4:42])
print(word[42:])

#If you need a different string, you should create a new one
print('J' + word[1:])
print(word[:2] + 'py')

#The built-in function len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
print(len(s))