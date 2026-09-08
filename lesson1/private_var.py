"""
Python Private Variables

Topics:
- _name
- __name
- Name mangling
- Why Python uses name mangling
"""


class Person:
    def __init__(self, name, age):
        # Non-public variable by convention
        self._name = name

        # Name-mangled variable
        self.__age = age

    def show_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self.__age}")


person = Person("Alex", 20)

person.show_info()

# _name is accessible, but it means:
# "This is intended for internal use."
print(person._name)

# __age cannot normally be accessed directly:
# print(person.__age)  # AttributeError

# Python changes __age internally to:
# _Person__age

print(person._Person__age)