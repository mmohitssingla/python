with open('write.txt', 'w') as write_file:
    write_file.write('Hey Peter, Python is awesome.')

with open('write.txt', 'a') as write_file:
    write_file.write('\nI am learning these topics:')


quotes = [
    '\nMachine Learning',
    '\nArtificial Intelligence'
    '\nRobotics'
]

with open('write.txt', 'a') as write_file:
    write_file.writelines(quotes)

