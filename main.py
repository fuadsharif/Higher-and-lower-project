import random
from game_data import data
from art import logo, vs

def option_formate(option):
    name= option["name"]
    desc= option["description"]
    country= option["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(user_guess,followers_a,followers_b):
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score=0
play= True
option_b= random.choice(data)
while play:
    option_a= option_b
    option_b= random.choice(data)
    if option_a==option_b:
        option_b= random.choice(data)

    print(f"Compare A: {option_formate(option_a)}")
    print(vs)
    print(f"Against B: {option_formate(option_b)}")
    guess= input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n" * 20)
    print(logo)

    f_a= option_a["follower_count"]
    f_b= option_b["follower_count"]
    is_correct= check_answer(guess,f_a,f_b)

    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play= False
