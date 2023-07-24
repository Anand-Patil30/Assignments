marks = int(input("Enter the marks: "))
if marks >= 80:
    print('Studen Got A Grade')
elif marks >= 60 and marks < 80:
    print('Studen Got B Grade')
elif marks >= 50 and marks < 60:
    print('Studen Got C Grade')
elif marks >= 45 and marks < 50:
    print('Studen Got D Grade')
elif marks > 25 and marks < 45:
    print('Studen Got E Grade')
else:
    print('Studen Got F Grade')
