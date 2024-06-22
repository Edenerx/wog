from app import welcome,start_play
from guess_game import guess_game_play
from currency_roulette_game import currency_roulette_game_play
from memory_game import memory_game_play

dict_game={1:"Guess Game",2:"Currency Roulette",3:"Memory Game"}


players_name=welcome()
game_diffecult,chosen_game, player_name=start_play(players_name)
if chosen_game == 1:
    guess_game_play(player_name, game_diffecult,chosen_game)
elif chosen_game == 2:
    currency_roulette_game_play(game_diffecult)
elif chosen_game == 3:
    memory_game_play(game_diffecult)
