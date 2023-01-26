import random
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] #i've taken a real life deck and simplified it to one "seed", where jack, queen and king are also worth 10
total = 0
ai_total = 0
draw = int(input("You will play against Coco. \nTo draw card (1) \nTo skip (2): \nTo quit (3)"))
print("-"*30)

while draw != 3:
    if draw == 1:
        card = random.choice(deck) #reference: https://www.w3schools.com/python/module_random.asp
        total += card
        print("your card is", card)
        print("your total is", total)
        if total > 21:
            print("Coco has won, uve lost")
            break
        if ai_total < 14:
            ai_card = random.choice(deck)
            ai_total += ai_card
            print("Coco's card is", ai_card)
            print("Coco's total is", ai_total)
            if ai_total > 21:
                print("You've won against Coco!")
                break
        else:
            print("Coco is feeling good about her score,", ai_total,",she skips")
        draw = int(input("to draw card (1) \n to skip (2): "))
        print("-"*30)
    elif draw == 2:
        if ai_total < 14:
            ai_card = random.choice(deck)
            ai_total += ai_card
            print("Coco's card is", ai_card)
            print("Coco's total is", ai_total)
            if ai_total > 21:
                print("You've won against Coco!")
                break
        else:
            print("Coco is feeling good about her score,", ai_total,",she skips")
            if #closest one to 21 wins, now just learn how to code that :skull:
        
        
        
        
        
        
        
        
