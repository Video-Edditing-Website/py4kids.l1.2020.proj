import os
import json


def read_review_file(file_name):
    name = open(file_name, "r")
    review = json.load(name)
    name.close()
    return review


def get_review_list():
    file_list = os.listdir("reviews")
    review_list = []
    for file_name in file_list:
        if file_name.endswith(".json"):
            d = read_review_file("reviews/"+file_name)
            review_list.append(d)
    return review_list

