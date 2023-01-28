import random
from blackjack_helpers import Player, Dealer

def print_headers(text, width=30):
	print("\n")
	print(width*'~')
	print(format(text,f'^{width}'))
	print(width*'~')
	print("\n")




# an interative prompt asks for how many players and a name for each player
input_players = ['mario', 'luigi']

#we build a list with players and dealer
players = []
for opponent in input_players:
	players.append(Player(opponent))

#we add the dealer
dealer = Dealer('mandrake')
players.append(dealer)

print_headers('Serving cards')

for p in players:
	for i in range(1,3):
		p.hit()
	p.show_hand()

print_headers('The game is open', 40)

for p in players:
	if isinstance(p, Dealer):
		p.show_hand(show_all=True)
	else:
		p.show_hand()
	p.play()

scores = [p.score for p in players]
highest = max(scores)