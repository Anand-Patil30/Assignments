list1=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
list1.sort(key=lambda e: (isinstance(e, str), e))
print(list1)
