from pathlib import Path

ROOT_PATH = "\\C:asdfasdf"
variable = "value"

PRICE = ""
USER = "Sebastian"


print(Path._remove_leading_dot)
Path._remove_leading_dot = "hejsan"


def a_function():
    print("Det här är en funktion!")

class MyClass: 
    def __init__(self):
        public_attribute = "PUBLIKT"
        _private_or_protected_attribute = ""
        __private_or_protected_attribute = ""

    def my_method(self):
        print("Det här är en metod!")


a_function()

my_class = MyClass()
my_class.my_method()

p = Path()
print(p.absolute())