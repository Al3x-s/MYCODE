# enumerate 
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(index, fruit)


#Memory View

data = bytearray(b"Hello, World!")
mv = memoryview(data)

# Accessing elements through memoryview
print(mv[0])  # 72 (ASCII value of 'H')
print(mv[7])  # 87 (ASCII value of 'W')

# Modifying data through memoryview
mv[7] = 65  # ASCII value of 'A'
print(data) # bytearray(b"Hello, Aorld!")


#filter

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(is_even, numbers))

print(filtered_numbers)


#zip

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

zipped_data = zip(names, ages, cities)

for data in zipped_data:
    print(data)

#hasattr

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

print(hasattr(person, "name"))  # True
print(hasattr(person, "age"))   # True
print(hasattr(person, "gender"))  # False
