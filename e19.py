# lorem_file = open('lorem.txt')
#
# # for line in lorem_file:
# #     print(line)
# #
# #
# # lorem_file.seek(0)
# #
# # lorem_text = lorem_file.readline()
# # print(lorem_text)
#
# lorem_file.seek(50)
# file_text = lorem_file.read(100)
# print(file_text)
#
# lorem_file.close()

def filter_names(line):
    return '>' not in line


with open('names.txt') as names:
    lines = names.readlines()
    print(list(filter(filter_names, lines)))
