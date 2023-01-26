default_deck = [1,2,3,4]

class player():
    """
    Class repesenting a single player. You can ovverride the
    deck to be used or use the default one.
    """
    def __init__(self, name, deck=default_deck):
        self.name = name
        self.score = 0
        self.hand = []
        self.deck = deck
        
    def greetings(self):
        print(f'yo, my name is {self.name}')
    
    def poppa_la_carta(self):
        self.deck.pop()
     
     
     
     
if __name__ == "__main__":
    players = []
    
    weird_deck = [3,3,3,3,3,3]


    mario = player('mario')
    players.append(mario)
    players.append(player('luigi'))
    players.append(player('weirdo', weird_deck))


    for player in players:
        print(f"{player.name}:{player.score}")
    
    for player in players:
        player.greetings()
    
    for player in players:
        print(player.deck)
    
    mario.poppa_la_carta()
    
    for player in players:
        print(player.deck)