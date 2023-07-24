class StringReverser:
    def reverse_words(self,string):
        words = string.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string


reverser = StringReverser()

string = input("Enter the string: ")
reversed_string = reverser.reverse_words(string)

print(f"Reversed String: {reversed_string}")
