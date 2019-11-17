import mile_stone_2_classes as ms2

playing = True

print("Welcome to the Black Jack")
str_input = input("Would you like to play a game? (y/n)")
while True:
    if str_input[0].lower() == "y":
        start = True
        break
    elif str_input[0].lower() == "n":
        start = False
        break
    else:
        print("Please enter y/n")


while start:
    #Create the deck and shuffle it
    game_deck = ms2.Deck()
    game_deck.shuffle()

    # Create player and dealer hand. Add cards to the hands
    player_money = ms2.Money()
    player_hand = ms2.Hand()
    dealer_hand = ms2.Hand()

    for i in range(2):
        player_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())

    while True:
        try:
            bet_input = int(input("Please take your bet "))
            if bet_input > player_money.total:
                print("You dont have enough money, you have {}".format(player_money.total))
            else:
                player_money.take_bet(bet_input)
                break
        except:
            print("Please provide an integer")

    #Show only one of the Dealer's cards, the other remains hidden 
    #Show both of the Player's cards
    print("\nYour cards: ")
    print(player_hand)
    print(player_hand.value())
    print("\nDealer's cards: ")
    print(dealer_hand.print_dealer())
    print(dealer_hand.value())


    #Ask the Player if they wish to Hit, and take another card
    hit = True
    while hit or dealer_hand.value() <= 17:

        #Player Turn
        got_answer = False
        while not got_answer:
            if hit:
                hit_stand_input = input("Would you like to Hit or Stay? (h/s) ")
            if hit_stand_input[0].lower() == "h":
                got_answer = True
                player_hand.add_card(game_deck.deal())
            elif hit_stand_input[0].lower() == "s":
               hit = False
               got_answer = True
            else:
                print("Please enter h/s")
        #szcenáriók
        if player_hand.value() > 21:
            ms2.dealer_wins(player_hand,dealer_hand,player_money)
            break
        if player_hand.value() == 21:
            ms2.player_wins(player_hand,dealer_hand,player_money)
            break
        
        # Dealer turn
        if dealer_hand.value() < 17:
            dealer_hand.add_card(game_deck.deal())
        else:
            dealer_stop = True
        
        #szcenáriók
        if dealer_hand.value() > 21:
            ms2.player_wins(player_hand,dealer_hand,player_money)
            break
        if dealer_hand.value() == 21:
            ms2.dealer(player_hand,dealer_hand,player_money)
            break

        
        print("\nYour cards: ")
        print(player_hand)
        print("\nDealer's cards: ")
        print(dealer_hand.print_dealer())
        if (not hit) and dealer_stop:
            if dealer_hand.value() > player_hand.value():
                ms2.dealer_wins(player_hand,dealer_hand,player_money)
                break
            elif dealer_hand.value() < player_hand.value():
                ms2.player_wins(player_hand,dealer_hand,player_money)
                break
    
    print("END OF THE GAME")
    str_input = input("Would you like to play new a game? (y/n)")
    while True:
        if str_input[0].lower() == "y":
            start = True
            break
        elif str_input[0].lower() == "n":
            start = False
            break
    else:
        print("Please enter y/n")

    
 


print("Good bye")
