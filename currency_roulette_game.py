import requests
import random

url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_6AWG0fUIn7zTdmUBEk4Xd3tDW9lnfdBtzqF3Fc8a'

responce=requests.get(url)
data=responce.json()
#print(data["data"]["ILS"])


def get_money_interval(game_diffecult):
    responce=requests.get(url)
    data=responce.json()
    ils_conversation=data["data"]["ILS"]
    random_num=random.randint(0,100)
    money_interval=ils_conversation*random_num
    min_ils_conversation=money_interval-game_diffecult
    max_ils_conversation=money_interval+game_diffecult
    print(f"Guess how much is ${random_num} in ILS")
    return max_ils_conversation, min_ils_conversation, money_interval

def get_guess_from_user():
    player_answer=int(input("Hi, Guess the converted vaule of a specified amount in USD "))
    return player_answer

def compare_results(player_answer,max_ils_conversation, min_ils_conversation,money_interval):
    if min_ils_conversation < player_answer < max_ils_conversation:
        print(f"you are correct the current conversation rate is {money_interval}")
    else:
        print(f"wrong, the current conversation rate is {money_interval} please try again")

def currency_roulette_game_play(game_diffecult):
    max_ils_conversation, min_ils_conversation, money_interval=get_money_interval(game_diffecult)
    player_answer=get_guess_from_user()
    compare_results(player_answer,max_ils_conversation, min_ils_conversation, money_interval)