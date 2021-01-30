def intro(comps):
    for key, val in comps.items():
        print(f'{key} has {val} system')


computers = {}

while True:
    name = input('enter name: ')
    system = input('enter computer: ')
    computers[name] = system

    another = input('enter another (y/n): ')
    if another == 'y':
        continue
    else:
        break

intro(computers)
