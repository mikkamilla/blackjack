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

    def is_21(self):
        return self.score == 21

    def hit(self):
        face, value = random.choice(list(self.deck.items()))
        self.hand.append(face)
        self.score += value

    def busted(self):
        if self.score >21:
            self.score = 0
            return True
        return False

    def play(self):
        while True:
            choice = input(f"{self.name}, it's your turn. \nTo hit(1) \nTo stand (2)\n Choose:")
            if choice == '1':
                self.hit()
                self.show_hand()
                if self.is_21():
                    print(f"That's it {self.name}, you got 21!")
                    break
                if self.busted():
                    print(f"Oh no, {self.name} has busted")
                    break
            elif choice == '2':
                break
            else:
                print("Invalid choice")

    def show_hand(self):
        print(self.name)
        print("\t", self.hand, self.score)

     

class Dealer(Player):

    def play(self, minimum=18):
        while self.score < minimum:
            print("Dealer hits")
            self.hit()
            self.show_hand(show_all=True)
        if self.busted():
            print(f"Oh no, the dealer {self.name} has busted")
        print(f"the dealer {self.name} stands")
        self.show_hand(show_all=True)

    def show_hand(self, show_all=False):
        revised_hand = ['X'] + self.hand[1:]
        print(f"{self.name} (Dealer)")
        if show_all:
            print("\t", self.hand, self.score)
        else:
            print("\t", revised_hand, "?")


  


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