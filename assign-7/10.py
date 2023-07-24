class Demo:
    pass

instance = Demo()
class_name = type(instance).__name__
print(f"The class name of the instance is: {class_name}")
