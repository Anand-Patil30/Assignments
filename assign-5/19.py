List1 = []
List2 = []
List3 = []
List4 = []
elements = int(input("Enter the no.of elements: "))
for i in range(elements):
    value = input("Enter the value: ")
    List1.append(value)
for item in List1:
    if item.isdigit():
        List2.append(int(item))
    else:
        try:
            List3.append(float(item))
        except ValueError:
            List4.append(item)
print(List2)
print(List3)
print(List4)
