year_of_service = int(input("Enter the year:"))
salary = int(input("Enter the salary:"))
bonus_amount = 0
if year_of_service > 5:
    bonus_amount = salary*0.05
else:
    bonus_amount = 0
print(bonus_amount)
