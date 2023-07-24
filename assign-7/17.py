list1 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
res = sorted(list1, key=lambda row: sum(row))
print(res)
