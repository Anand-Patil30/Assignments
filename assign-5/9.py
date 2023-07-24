quantity = int(input("Enter the quantity:"))
cost = quantity*100
res = 0
if cost > 1000:
    res = cost*0.10
else:
    res = cost
print(res)
