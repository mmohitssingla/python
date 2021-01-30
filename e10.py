class Person:

    def __init__(self):
        self.name = 'Mohit'
        self.age = 30
        self.location = 'Maur'

    def running(self):
        return f'{self.name} is running very fast.'


man1 = Person()
print(f'Name : {man1.name}')
print(f'Age : {man1.age}')
print(f'Location : {man1.location}')
print(man1.running())

