# def greet(name, time):
#     print(f"Hello {name}, Good {time}")
#
# name = input('enter your name: ')
# time = input('enter the time: ')
#
# greet(name, time)

def area(radius):
    return 3.142 * radius * radius
def vol(area, length):
    print(area * length)


radius = int(input('enter radius: '))
length = int(input('enter length: '))
vol(area(radius), length)