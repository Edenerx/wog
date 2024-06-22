import random
import time
import os


def generate_sequence(game_diffecult): #Generates a list of random numbers between 1 and 101, with a length equal to the difficulty.
    random_numbers=[]
    for i in range(game_diffecult):
        random_number=random.randint(0,101)
        random_numbers.append(random_number)
    print(random_numbers)
    time.sleep(0.7)
    os.system('cls')
    return random_numbers

def get_list_from_user(game_diffecult): #Prompts the user to input a list of numbers matching the length of the generated sequence.
    players_numbers=[]
    for i in range(game_diffecult):
        players_number=int(input(f"Hi,please provide the {i+1} number on the list "))
        players_numbers.append(players_number)
    print(players_numbers)
    return players_numbers

def is_list_equal(random_numbers,players_number): #Compares two lists to verify if they are identical, returning True if they match and False otherwise.
    if random_numbers == players_number:
        print(f"You Won!")
    else:
        print(f"You Lose!")

def memory_game_play(game_diffecult): #Executes the game by invoking the functions above and returns True if the user wins, and False if the user loses.
    random_numbers=generate_sequence(game_diffecult)
    players_number=get_list_from_user(game_diffecult)
    is_list_equal(random_numbers,players_number)
