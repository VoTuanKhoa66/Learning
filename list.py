squares = [1,2,3,4,5,6]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares + [7,8,9,10])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # replace the wrong value
print(cubes)

cubes.append(216)
cubes.append(7**3)
print(cubes)

rgb = ["Red", "Blue", "Green"]
rgba = rgb
rgba.append("Alph")
print(rgba)

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(f"Correct rgba: {correct_rgba}")
print(rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = ['C', 'D', 'E']

#now remove them 
letters[2:5] = []
print(f"Remove C D E: {letters[2:5]}")
#clear the list
letters[:] = []
print(f"Clear list: {letters[:]}")

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0])
print(x[0][1])

