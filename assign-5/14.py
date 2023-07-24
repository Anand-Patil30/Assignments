List1 = []
elements = int(input("Enter the no.of elements: "))
for i in range(elements):
    number = int(input("Enter the number: "))
    List1.append(number)
for num in List1:
    product = 1
    for i in range(1, 11):
        product = num*i
        print(product)
    print("\n")
