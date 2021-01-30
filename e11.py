class Person:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def running(self):
        return f'{self.name} is running very fast.'


man1 = Person('Mohit', 30, 'Maur')
print(f'Name : {man1.name}')
print(f'Age : {man1.age}')
print(f'Location : {man1.location}')
print(man1.running())

man2 = Person('Harry', 25, 'London')
print(f'Name : {man2.name}')
print(f'Age : {man2.age}')
print(f'Location : {man2.location}')
print(man2.running())
