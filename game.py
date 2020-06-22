import random
from black_jack_class_library import WinStatus
from black_jack_class_library import Hand
from black_jack_class_library import Player
from black_jack_class_library import BlackJackConst
from black_jack_class_library import Deck

def create_turn(player_hand, deck):
    player_hand.cards.append(deck.get_card())

def check_hand(hand = Hand()):
    hand_sum = 0;
    a_counter = 0
    for card in hand.cards:
        hand_sum += card.value
        if card.name == 'A':
            a_counter += 1
    if hand_sum > BlackJackConst.LIMIT_POINT:
        while a_counter > 0 and hand_sum > BlackJackConst.LIMIT_POINT:
            hand_sum -= BlackJackConst.ACE_DIFFERENCE
            a_counter -= 1
    return hand_sum

def finish_game(winStatus = WinStatus.NOT_DEFINED, player_result = 0, dealer_hand = Hand(), deck = Deck()):
    if winStatus == WinStatus.LOSE:
        return WinStatus.LOSE
    else:
        dealer_result = get_dealer_turns(dealer_hand, deck)
        if dealer_result > BlackJackConst.LIMIT_POINT or dealer_result < player_result:
            return WinStatus.WIN
        elif dealer_result > player_result:
            return WinStatus.LOSE
        elif dealer_result == player_result:
            return WinStatus.DRAW

def get_dealer_turns(dealer_hand = Hand(), deck = Deck()):
    while True:
        if(check_hand(dealer_hand)) >= BlackJackConst.DEALER_TURN_LIMIT:
            return check_hand(dealer_hand)
        else:
            create_turn(dealer_hand, deck)

if __name__ == "__main__":
    deck = Deck()
    random.shuffle(deck.deck)

    name = input("Provide your name: ")
    value = int(input("Provide your balance: "))

    player = Player(name, value)
    dealer = Player("dealer", 100500)

    while player.balance > 0:
        result = ''
        bet = int(input("Make your bet"))
        if (player.balance - bet < 0):
            print("You haven't enough money")
            continue
        dealer_hand = Hand(dealer, deck, is_dealer=True)
        player_hand = Hand(player, deck, is_dealer=False)

        while check_hand(player_hand) <= 21:
            print(player_hand)
            player_definition = input("Do you wanna another card? (y/n)")
            if player_definition == 'y':
                create_turn(player_hand, deck)
                print(dealer_hand)
                print(player_hand)
            elif player_definition == 'n':
                print(dealer_hand)
                print(player_hand)
                result = finish_game(WinStatus.NOT_DEFINED, check_hand(player_hand), dealer_hand, deck)
                break
            else:
                print("enter 'y' or 'n'")
                continue

        if check_hand(player_hand) > 21:
            result = WinStatus.LOSE

        print(dealer_hand)
        print(player_hand)

        if result == WinStatus.WIN:
            player.balance += bet
        elif result == WinStatus.LOSE:
            player.balance -= bet

        print(result)
        print(player.balance)

    print("You lose")