num=int(input("Enter the number of elements:"))
if num==0:
    print("Finish")
else:
    sumofnumbers=0
    numlist=[]
    for i in range(num):
        number=int(input("Enter the elements:"))
        numlist.append(number)
    for i in range(len(numlist)):
        sumofnumbers+=numlist[i]
    print("Sum of the numbers is:",sumofnumbers)   
    print("Average of the numbers is:",sumofnumbers/num)