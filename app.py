
dict_game={1:"Guess Game",2:"Currency Roulette",3:"Memory Game"}
players_name=""


def welcome():
    players_name=input("What is your name: ")
    print(f"Hi {players_name} and welcome to the World of Games: The Epic Journey")
    return players_name

def start_play(players_name):
    print("1 Guess Game - guess a number and see if you chose like the computer\n" \
    "2 Currency Roulette - Try and guess the value of a random amount of USD in ILS\n" \
    "3 Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    user_game_choose=input(f"Hi {players_name} Please choose the number assoiste with the game that you wouldlike to play: ")
    user_game_choose=int(user_game_choose)
    if user_game_choose in dict_game:
        print(f"You choose the game {dict_game[user_game_choose]}")
        game_diffeculty=input("Choose diffeculty between 1-5 ")
        game_diffeculty=int(game_diffeculty)
        if type(game_diffeculty)==int and 0 < game_diffeculty < 6:
            return game_diffeculty, user_game_choose,players_name
        else:
            print("You provided an invalid choise")
            start_play(players_name)
    else:
        print("You provided an invalid choise")
        start_play(players_name)

