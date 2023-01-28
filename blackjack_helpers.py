import random
from decks import default_deck

class Player():
    """
    Class repesenting a single player. You can ovverride the
    deck to be used or use the default one.
    """
    def __init__(self, name, deck=default_deck):
        self.name = name 
        self.score = 0
        self.hand = []
        self.deck = deck



if __name__ == "__main__":
    players = []
    
    weird_deck = [3,3,3,3,3,3]


    mario = Player('mario')
    players.append(mario)
    players.append(Player('luigi'))
    players.append(Player('weirdo', weird_deck))


    for player in players:
        print(f"{player.name}:{player.score}")
    
    for player in players:
        player.greetings()
    
    for player in players:
        print(player.deck)
    
    mario.poppa_la_carta()
    
    for player in players:
        print(player.deck)