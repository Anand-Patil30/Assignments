list1=['red', 'black', 'white', 'green', 'orange']
substr=input("Enter the substring to search: ")
res=list(filter(lambda x:substr in x, list1))
print(res)
