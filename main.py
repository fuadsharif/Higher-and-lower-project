import random

from game_data import data

def option_a_i(info):

    details= f"Compare A: {info['name']}, a {info['description']}, from {info['country']}"
    return details


def option_b_i(info):
    details= f"Against B: {info['name']}, a {info['description']}, from {info['country']}"
    return details


def option_a_f(followers):
    follower_count= followers["follower_count"]
    return follower_count

def option_b_f(followers):
    follower_count= followers["follower_count"]
    return follower_count

def compare(a,b):
    








list_item_a= random.choice(data)
list_item_b= random.choice(data)
f_a= option_a_f(list_item_a)
f_b= option_b_f(list_item_b)

print(option_a_i(list_item_a))
print(option_b_i(list_item_b))






