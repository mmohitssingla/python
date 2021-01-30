class Person:
    color = 'Brown'

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def running(self):
        return f'{self.name} is running very fast.'

    @classmethod
    def common(cls):
        return f'All persons are {cls.color} in Color.'

    @staticmethod
    def walk(speed='5 Km/Hour'):
        return f'The person walks at {speed}.';


man1 = Person('Mohit', 30, 'Maur')
# print(f'Name : {man1.name}')
# print(f'Age : {man1.age}')
# print(f'Location : {man1.location}')
# print(man1.running())
# print(man1.color)
print(Person.common())
print(Person.walk('very high speed'))
