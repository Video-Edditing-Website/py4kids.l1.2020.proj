import os
import json

def read_review_file(file_name):
    name = open(file_name, "r")
    review = json.load(name)
    name.close()
    return review


file_list = os.listdir("reviews")
for file_name in file_list:
    if file_name.endswith(".json"):
        d = read_review_file("reviews/"+file_name)
        print(d)