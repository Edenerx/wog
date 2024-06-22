from app import welcome,start_play
import random

game_diffecult_dict={1:20,2:40,3:60,4:80,5:100}
dict_game={1:"Memory Game",2:"Guess Game",3:"Currency Roulette"}



def generate_number(game_diffecult):
    random_number=random.randint(0,game_diffecult_dict[game_diffecult]) 
    return random_number

def get_guess_from_user(game_diffecult):
    players_answer=input(f"Guess the number between 0-{game_diffecult_dict[game_diffecult]} ")
    return int(players_answer)

def compare_results(players_answer,random_number):
    if random_number==players_answer:
        print(f"You Won!, the correct number was {random_number}")
    else:
        print(f"You Lose!, the correct number was {random_number}")

def guess_game_play(player_name,game_diffecult,chosen_game):
    print(f"Hi {player_name}, You choose to play {dict_game[chosen_game]} in the diffecult level {game_diffecult}")
    random_number=generate_number(game_diffecult)
    players_answer=get_guess_from_user(game_diffecult)
    compare_results(players_answer,random_number)