side1 = int(input("Enter the side1 length: "))
side2 = int(input("Enter the side2 length: "))
side3 = int(input("Enter the side3 length: "))

if side1 == side2 == side3:
    print("it is Equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("it is Isosceles.")
elif side1 != side2 != side3:
    print("it is Scalene.")
