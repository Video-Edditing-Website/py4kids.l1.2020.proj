import os
my_dir= os.path.join('.')
def read_file_as_lines(file_name):
    file = open(file_name, "r")
    return file.readlines()
print("My directory is [{}]".format(my_dir))
my_dir = os.path.abspath(my_dir)
print("My directory is [{}]".format(my_dir))
file_list = os.listdir()
for file_name in file_list:
    if not os.path.isdir(file_name):
        if file_name.endswith(".py") :
            print("{} is python file".format(file_name))
file_contents = read_file_as_lines("README.md")
for line in file_contents:
    print(line , end="")