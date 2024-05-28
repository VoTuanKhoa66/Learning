print(17 / 3) #classic division returns a float
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # returns the reamainder of the division 

# Since "**" has higher precedence than "-", ex -3**2 = -9 , so can use () (-3)**2 = 9 
print(5 ** 2) # 5 squared
print(2 ** 7) # 2 to the power of 7
print((-3) ** 2)

#The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt
width = 20
height = 5 * 9
print(width * height)

tax = 12.5 / 100
price = 100.50
print(price * tax)
_ = price * tax
print(price + _)
print(round(_, 2))


