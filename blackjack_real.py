import random
import math
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] #i've taken a real life deck and simplified it to one "seed", where jack, queen and king are also worth 10
x = 0
y = 0
z = 0

mode = int(input("Hello and welcome to simplified blackjack, please enter (1) for single player, (2) for multiplayer, (3) for simulation play and (4) to quit game"))
while mode != 4:
    if mode == 1: #singleplayer
        if x == 0:
            total = 0
            ai_total = 0
            draw = int(input("You will play against Coco. \nTo draw card (1) \nTo skip (2): \nTo quit (3): "))
            print("-"*30)
            while draw != 3:
                if draw == 1: #if player decides to draw card
                    card = random.choice(deck) #reference: https://www.w3schools.com/python/module_random.asp
                    total += card
                    print("your card is", card)
                    print("your total is", total)
                    print("-"*30)
                    if total > 21: #if player score goes over 21, player loses
                        print("You went over 21, Coco has won against you with a score of ", ai_total)
                        x = 1 #for 'break' to work i needed to change the directory of the while loop, from asking the player to either draw a card or skip to asking the player which mode they'd like to choose
                        break
       
                    if ai_total < 17: #if ai score is less than 17, ai draws a card
                        ai_card = random.choice(deck)
                        ai_total += ai_card
                        print("Coco's card is", ai_card)
                        print("Coco's total is", ai_total)
                        print("-"*30)
                        if ai_total > 21: #if ai score goes over 21, ai loses
                            print("Coco went over 21, you've won against Coco with a score of", total)
                            x = 1
                            break
                    else: #if ai score is 17 or over, ai skips turn
                        print("Coco is happy with her score", ai_total, "and she decides to skip")
                        print("-"*30)
           
                    draw = int(input("To draw card (1) \nTo skip (2): \nTo quit (3): ")) #asks player if they'd like to draw a card or skip
                    print("-"*30)
                                   
                elif draw == 2: #if player decides to skip turn
                    if ai_total < 17: #if ai score is less than 17, ai draws a card
                        ai_card = random.choice(deck)
                        ai_total += ai_card
                        print("Coco's card is", ai_card)
                        print("Coco's total is", ai_total)
                        print("-"*30)
                    else:
                        if ai_total > 21: #if ai score goes over 21, ai loses
                            print("Coco went over 21, you've won against Coco with a score of", total)
                            x = 1
                            break
                        print("Coco is happy with her score", ai_total, "and she decides to skip") #if ai score is less than 21 but more than 16 ai skips
                        diff_player = 21 - total
                        diff_ai = 21 - ai_total
                        if diff_player > diff_ai: #as both player and ai have skipped, closest player to 21 wins
                            print("Coco has won against you with a score of",ai_total, "as she's closer to 21 and your score was", total)
                            x = 1
                            break
                        elif diff_ai > diff_player:
                            print("you've won against Coco with a score of", total, "as you're closer to 21 and her score was", ai_total)
                            x = 1
                            break
                        else: #elif diff_ai == diff_player
                            print("there has been a draw, your scores are", total, ai_total)
                            x = 1
                            break
                else:
                    print("Invalid input")
                    draw = int(input("You will play against Coco. \nTo draw card (1) \nTo skip (2): \nTo quit (3): "))
                    print("-"*30)
                   
            x = 0
            mode = int(input("Hello and welcome to simplified blackjack, please enter (1) for single player, (2) for multiplayer, (3) for simulation play and (4) to quit game"))
           
           
           
    elif mode == 2: #multiplayer
        if y == 0:
            player_one_total = 0
            player_two_total = 0
            player_one = input("State player 1 name: ")
            player_two = input("State player 2 name: ")
            print(player_one,"'s turn: (score :",player_one_total,")")
            draw_multi = int(input("To draw card (1) \nTo skip (2): \nTo quit (3): "))
            print("-"*30)
            while draw_multi != 3:
               
               
                if draw_multi == 1: #if 1 player decides to draw card
                    card_one = random.choice(deck)
                    player_one_total += card_one
                    print(player_one,"'s card is", card_one)
                    print(player_one,"'s total is", player_one_total)
                    print("-"*30)
                    if player_one_total > 21: #if player 1 score goes over 21, player 1 loses, player 2 wins
                        print("You went over 21,",player_two," has won against you with a score of ", player_two_total)
                        y = 1
                        break
                   
                   
                   
                elif draw_multi == 2: #if player 1 skips
                    print(player_one,"has decided to skip their turn")
                    while z == 0:
                        print(player_two,"'s turn: (score:",player_two_total,")")
                        draw_multi_two = int(input("To draw card (1) \nTo skip (2): "))
                        if draw_multi_two == 1: #if 2 player decides to draw card
                            card_two = random.choice(deck)
                            player_two_total += card_two
                            print("-"*30)
                            print(player_two,"'s card is", card_two)
                            print(player_two,"'s total is", player_two_total)
                            print("-"*30)
                            if player_two_total > 21: #if player 1 score goes over 21, player 1 loses, player 2 wins
                                print("You went over 21,",player_one," has won against you with a score of ", player_one_total)
                                y = 1
                                z = 1
                                break

                        elif draw_multi_two == 2: #if player 2 decides to skip AFTER player 1 has skipped
                            diff_player1 = 21 - player_one_total
                            diff_player2 = 21 - player_two_total
                            if diff_player1 < diff_player2:
                                print(player_one," has with a score of", player_one_total,"as it was closer to 21 and", player_two,"has a score of", player_two_total)
                                y = 1
                                z = 1
                                break
                            elif diff_player1 > diff_player2:
                                print(player_two," has with a score of", player_two_total,"as it was closer to 21 and", player_one,"has a score of", player_one_total)
                                y = 1
                                z = 1
                                break
                            else:
                                print("there was a draw with the score of", player_one_total)
                                y = 1
                                z = 1
                                break
                                #could ask to want to finish w a coin flip or keep the draw
                    break
                       
                print(player_two,"'s turn: (score:",player_two_total,")")
                draw_multi_two = int(input("To draw card (1) \nTo skip (2): "))
                print("-"*30)
                if draw_multi_two == 1: #if player 2 decides to draw card
                    card_two = random.choice(deck)
                    player_two_total += card_two
                    print(player_two,"'s card is", card_two)
                    print(player_two,"'s total is", player_two_total)
                    print("-"*30)
                    if player_two_total > 21: #if player 2 score goes over 21, player 2 loses, player 1 wins
                        print("You went over 21,",player_one," has won against you with a score of ", player_one_total)
                        y = 1
                        break
                elif draw_multi_two == 2: #if player 2 decides to skip
                    print(player_two,"has decided to skip their turn")
                    while z == 0:
                        print(player_one,"'s turn: (score:",player_one_total,")")
                        draw_multi = int(input("To draw card (1) \nTo skip (2): "))
                        if draw_multi == 1: #if 1 player decides to draw card AFTER player 2 has skipped
                            card_one = random.choice(deck)
                            player_one_total += card_one
                            print("-"*30)
                            print(player_one,"'s card is", card_one)
                            print(player_one,"'s total is", player_one_total)
                            print("-"*30)
                            if player_one_total > 21: #if player 1 score goes over 21, player 1 loses, player 2 wins
                                print("You went over 21,",player_two," has won against you with a score of ", player_two_total)
                                y = 1
                                z = 1
                                break

                        elif draw_multi == 2: #if player 1 decides to skip AFTER player 2 has skipped
                            diff_player1 = 21 - player_one_total
                            diff_player2 = 21 - player_two_total
                            if diff_player1 < diff_player2:
                                print(player_one," has with a score of", player_one_total,"as it was closer to 21 and", player_two,"has a score of", player_two_total)
                                y = 1
                                z = 1
                                break
                            elif diff_player1 > diff_player2:
                                print(player_two," has with a score of", player_two_total,"as it was closer to 21 and", player_one,"has a score of", player_one_total)
                                y = 1
                                z = 1
                                break
                            else:
                                print("there was a draw with the score of", player_one_total)
                                y = 1
                                z = 1
                                break
                                #could ask to want to finish w a coin flip or keep the draw
                    break
                   
                   
                                   
                   
                   
                print(player_one,"'s turn: (score :",player_one_total,")")  
                draw_multi = int(input("To draw card (1) \nTo skip (2):"))
                print("-"*30)
               
            y = 0
            z = 0
            mode = int(input("Hello and welcome to blackjack, please enter (1) for single player, (2) for multiplayer, (3) for simulation play and (4) to quit game"))