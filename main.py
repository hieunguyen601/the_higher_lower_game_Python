from art import logo
from art import vs
from data import data
import random
def assign():
    return random.choice(data)
def compare(p1,p2,user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']
    max= ''

    if sum1 > sum2:
        max= p1['name']
    elif sum1 < sum2:
        max = p2['name']

    if max == user_input:
        return True
    else:
        return False
def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        while still_guessing:
            print(logo)
            person1 = assign()
            person2 = assign()
            if score > 0:
                person1 = person2
                person2 = assign()

                if person1 == person2:
                    person2 = assign()
            print(f"Name: {person1['name']}, Description: {person1['description']}, Followers: {person1['follower_count']}")
            print(vs)
            print(f"Name: {person2['name']}, Description: {person2['description']}, Followers: {person2['follower_count']}")

            print("________________________________________")
            print(f"Your current score is: {score}")
            print("________________________________________")

            guess = input("Enter name of person with the higher followers: ")
            if compare(person1, person2, guess):
                score +=1
                print("Correct")
            else:
                still_guessing = False
                print("Incorrect")
                break
        play_again = input("Would you like to play again? (yes/no) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "no":
            playing_game = False
            print("Exiting game")
        else:
            playing_game = False
            print("Invalid input. Please try again!")

want_to_play = input(f"Would you like to play Higher Lower game? yes/no ").lower()

if want_to_play == "yes":
    play_higher_lower()
elif want_to_play == "no":
    print("Program exits succesfully")
else:
    print("Invalid Input")


