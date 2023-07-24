list = []
stringList = []
num = int(input("Enter the number of strings : "))
for i in range(num):
    names = input("Enter the string : ")
    stringList.append(names)

print("The length of the longest string is : ")
for name in range(len(stringList)):
    a = len(stringList[name])
    list.append(a)
print(max(list))

