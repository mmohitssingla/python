def remove_fails(grade):
    return grade != 'F'


grades = ['A', 'B', 'A', 'F', 'C', 'F']

print(list(filter(remove_fails, grades)))