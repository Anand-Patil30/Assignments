number_of_class_held = int(input("Enter the no.of class held: "))
number_of_class_attended = int(input("Enter the no.of class attended: "))


print("Total no.of class held is :", number_of_class_held)
print("Total no.of class attended is :", number_of_class_attended)

percentage = (number_of_class_attended/number_of_class_held)*100

print(f'Attendence percentage is {percentage}')

if percentage > 75:
    print("Student is allowed to sit in class.")
else:
    print("Student is not allowed to sit in class.")
