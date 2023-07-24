List1 = []
elements = int(input("Enter the no.of elements: "))
for i in range(elements):
    number = int(input("Enter the number: "))
    List1.append(number)
sum_of_numbers = sum(List1)
avg = sum_of_numbers/elements
print(avg)
