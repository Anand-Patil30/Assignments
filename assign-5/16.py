List1=[]

elements=int(input("Enter the no.of elements: "))
for i in range(elements):
    number=int(input("Enter the numbers: "))
    List1.append(number)
    
print(List1)    
key=int(input("Enter the number to delete: "))
List1 = [num for num in List1 if num != key]
print("After deletion: ",List1)