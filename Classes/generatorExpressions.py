sq = sum(i*i for i in range(10))                 # sum of squares
print(sq)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
dp = sum(x*y for x,y in zip(xvec, yvec))  
print(dp)       # dot product

data = 'golf'
r = list(data[i] for i in range(len(data)-1, -1, -1))
print(r)