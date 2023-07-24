list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
        52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49,
        51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
dividedby_4 = []
dividedby_6 = []
dividedby_8 = []
dividedby_10 = []
dividedby_3 = []
dividedby_5 = []
dividedby_7 = []
dividedby_9 = []
for num in list1:
    if num % 4 == 0:
        dividedby_4.append(num)
    if num % 6 == 0:
        dividedby_6.append(num)
    if num % 8 == 0:
        dividedby_8.append(num)
    if num % 10 == 0:
        dividedby_10.append(num)

for num in list2:
    if num % 3 == 0:
        dividedby_3.append(num)
    if num % 5 == 0:
        dividedby_5.append(num)
    if num % 7 == 0:
        dividedby_7.append(num)
    if num % 9 == 0:
        dividedby_9.append(num)

print("Numbers divisible by 4:", dividedby_4)
print("Numbers divisible by 6:", dividedby_6)
print("Numbers divisible by 8:", dividedby_8)
print("Numbers divisible by 10:", dividedby_10)
print("Numbers divisible by 3:", dividedby_3)
print("Numbers divisible by 5:", dividedby_5)
print("Numbers divisible by 7:", dividedby_7)
print("Numbers divisible by 9:", dividedby_9)