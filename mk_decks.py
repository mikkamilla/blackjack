def get_value_from_face(card):
    num = card.split(' ')[0]
    try:
        value = int(num)
    except ValueError:
        value = 10
    return value

undressed_cards = [i for i in range(1,11)]
seeds = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

faces = [str(i) for i in undressed_cards] + ['J', 'Q', 'K']
faces_and_seeds = [f'{face} {seed}' for face in faces for seed in seeds]

default_deck = {face:get_value_from_face(face) for face in faces_and_seeds}