numlist = int(input("Enter the number of elements:"))
List = []
for i in range(numlist):
    numbers = int(input("Enter the numbers:"))
    List.append(numbers)
count = 0
for i in range(len(List)):
    if List[i] > 30:
        count += 1
print(count)
