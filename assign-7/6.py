class Power_Finder:
    def power_of(self,base,power):
        result=pow(base,power)
        print(result)

base=int(input("Enter the base value: "))

power=int(input("Enter the power value: "))

Result=Power_Finder()
Result.power_of(base,power)


