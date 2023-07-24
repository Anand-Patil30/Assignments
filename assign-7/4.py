class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair_indices(self):
        num_to_index = {}
        for idx, num in enumerate(self.numbers):
            complement = self.target - num
            if complement in num_to_index:
                return num_to_index[complement], idx
            num_to_index[num] = idx
        return None

if __name__ == "__main__":
    numbers = [90, 20, 10, 40, 50, 60, 70]
    target = 50
    pair_finder = PairFinder(numbers, target)
    result = pair_finder.find_pair_indices()
    if result:
        print(f"Output: {result[0]}, {result[1]}")
    else:
        print("No pair found.")
