class StringReverse:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_Reversed_string(self):
        print("Reversed string:", self.string[::-1])


Demo = StringReverse()
Demo.get_string()
Demo.print_Reversed_string()
