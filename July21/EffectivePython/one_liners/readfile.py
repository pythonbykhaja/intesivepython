from os import close


#file_name = 'data/info.txt'

# file_object = open(file_name)
# lines = []
# for line in file_object:
#     lines.append(line.strip())
# print(lines)
# file_object.close()

print([line.strip() for line in open('data/info.txt')])