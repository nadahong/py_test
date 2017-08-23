class Person:
    name = 'kim'
    gender = 'male'
    address = 'seoul'

    def __init__(self):
        self.__address = 'kim'

    def print(self):
        print('aaa')

    def get_name(self):
        return self.name

