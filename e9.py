def intro(comps):
    systems = list(comps.values())
    for comp in set(systems):
        num = systems.count(comp)
        print(f'There are {num} {comp} systems.')


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
