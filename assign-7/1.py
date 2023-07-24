class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def int_to_roman(self, num):
        if not isinstance(num, int) or not (0 < num < 4000):
            raise ValueError(
                "Invalid input.")
        roman_numeral = ''
        for value, symbol in self.roman_numerals.items():
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

    def roman_to_int(self, roman2):
        roman_numerals_inverse = {a: b for b, a in self.roman_numerals.items()}
        num = 0
        prev_value = 0
        for symbol in reversed(roman2):
            value = roman_numerals_inverse.get(symbol, 0)
            if value < prev_value:
                num -= value
            else:
                num += value
            prev_value = value
        return num


converter = RomanConverter()

num = int(input("Enter The Number To be Converted : "))
roman = converter.int_to_roman(num)
print(f"{num} in Roman numerals: {roman}")

roman2 = input("Enter The Roman Number To be Converted : ")
integer = converter.roman_to_int(roman2)
print(f"{roman2} in integer form: {integer}")
