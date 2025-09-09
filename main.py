def play_game():
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    player_cards = []
    computer_cards = []
    user_reply = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
    if user_reply == "y":
        player_card_1 = random.choice(cards)
        player_card_2 = random.choice(cards)
        computer_card_1 = random.choice(cards)
        computer_card_2 = random.choice(cards)
        player_cards.append(player_card_1)
        player_cards.append(player_card_2)
        computer_cards.append(computer_card_1)
        computer_cards.append(computer_card_2)
        score = player_card_1 + player_card_2
        if sum(player_cards) > 21 and 11 in player_cards:
            player_cards[player_cards.index(11)] = 1

        if sum(computer_cards) > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1

        if score == 21:
            print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
            print("Congratulations, you won! Blackjack!")
            play_game()

        while sum(player_cards) < 21:

            print(f"Your cards:  {player_cards} current score= {sum(player_cards)}")
            print("Computer's first card: ", computer_card_1)
            take_card = input("Type 'y' to get another card, type 'n' to pass:")
            if take_card == "y":
                player_cards.append(random.choice(cards))
                if sum(player_cards) > 21 and 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1

            if take_card == "n":
                while not sum(computer_cards) > 16:
                    computer_cards.append(random.choice(cards))
                    if sum(computer_cards) > 21 and 11 in computer_cards:
                        computer_cards[computer_cards.index(11)] = 1

                if sum(computer_cards) > 21:
                    print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
                    print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
                    print("Congratulations, you won! Computer went over!")
                    play_game()
                elif computer_cards[0] + computer_cards[1] == 21:
                    print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
                    print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
                    print("Sorry! You lose! Computer's Blackjack! :(")
                    play_game()
                else:
                    if sum(computer_cards) > sum(player_cards):
                        print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
                        print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
                        print("Sorry! Computer wins! :(")
                        play_game()
                    elif sum(computer_cards) < sum(player_cards):
                        print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
                        print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
                        print("Congratulations, you won!")
                        play_game()

        print(f"Your final hand:  {player_cards} final score = {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards} , final score: {sum(computer_cards)}")
        print("You went over! You lose! :(")
        play_game()
    else:
        breakpoint()
play_game()