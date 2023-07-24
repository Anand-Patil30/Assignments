List1 = []
while True:
    number = input("Enter the number or press q to quit: ")
    if number == 'q':
        break
    else:
        List1.append(int(number))
product = 1
for i in range(1, len(List1)):
    product *= List1[i]
sum_of_num = sum(List1)
count = 0
for i in range(1, len(List1)+1):
    count += 1
try:
    avg = sum_of_num/count
    print(product)
    print(avg)
except ZeroDivisionError:
    print("Total count is 0")

