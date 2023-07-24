class Subsets:
    def __init__(self):
        self.subsets = []
        
    def add(self, num, current, start):
        self.subsets.append(list(current))
        for i in range(start, len(num)):
            current.append(num[i])
            self.add(num, current, i + 1)
            current.pop()    

    def subset(self, num):
        self.subsets = []
        self.add(num, [], 0)
        return self.subsets



set=[]
input_sample = int(input("Enter the no.of list elements: "))
for i in range(input_sample):
    value=int(input("Enter the elements: "))
    set.append(value)
gen = Subsets()
result = gen.subset(set)
print(result)
