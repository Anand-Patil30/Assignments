from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

total_dict = Counter(d1) + Counter(d2)
print(total_dict)
