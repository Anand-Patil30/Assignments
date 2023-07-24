elements = int(input("Enter the no.of elements: "))
List1 = []
List2 = []
for i in range(elements):
    numbers = int(input("Enter the numbers: "))
    List1.append(numbers)
print(List1)
for i in range(1, len(List1)+1):
    i = i*i
    List2.append(i)
print(List2)
