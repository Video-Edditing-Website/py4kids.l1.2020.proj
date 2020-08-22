import os

my_dir= os.path.join('.')

def read_file_as_lines(file_name):
    file = open(file_name, "r")
    return file.readlines()


file_list = os.listdir("reviews")

for file_name in file_list:
    if not os.path.isdir(file_name):
        if file_name.endswith(".py") :
            print("{} is python file".format(file_name))
