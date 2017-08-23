class Animal:

    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry


cat = Animal('야옹이', 3, True)
dog = Animal('강아지', 4, False)

animal_list = [cat, dog]

animal_list_pythonic = [
    {'name': '야옹이', 'age': 3, 'is_hungry': True},
    {'name': '강아지', 'age': 4, 'is_hungry': False}
]


print(cat.name)





