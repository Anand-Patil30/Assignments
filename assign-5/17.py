List1 = []
List2 = []
List3 = []

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 101):
    if i % 2 == 0:
        List1.append(i)
    elif i % 2 != 0:
        if is_prime(i):
            List3.append(i)
        else:
            List2.append(i)
print(List1)
print(List2)
print(List3)
