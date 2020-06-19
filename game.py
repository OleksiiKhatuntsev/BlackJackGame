import random
import enum

class WinStatus(enum.Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

class Player():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Card():

    def __init__(self, name, value, is_hidden):
        self.name = name
        self.value = value
        self.is_hidden = is_hidden

    def __str__(self):
        return f"name : {self.name}, value: {self.value}"

class Hand():

    def __init__(self, player):
        self.player = player
        self.cards = []
        card = deck.pop()
        if player.name == 'dealer':
            card.is_hidden = True
        self.cards.append(card)
        self.cards.append(deck.pop())

    def __str__(self):
        result = f"{self.player.name}: "
        for card in self.cards:
            if card.is_hidden:
                result += ('* ')
            else:
                result += (card.name + ' ')
        return result

def create_turn(player_hand):
    player_hand.cards.append(deck.pop())

def check_hand(hand):
    hand_sum = 0;
    a_counter = 0
    for card in hand.cards:
        hand_sum += card.value
        if card.name == 'A':
            a_counter += 1
    if hand_sum > 21:
        while a_counter > 0 and hand_sum > 21:
            hand_sum -= 10
            a_counter -= 1
    return hand_sum

def finish_game(status, player_result, dealer_hand):
    if not status:
        return WinStatus.LOSE
    else:
        dealer_result = get_dealer_turns(dealer_hand)
        if dealer_result > 21 or dealer_result < player_result:
            return WinStatus.WIN
        elif dealer_result > player_result:
            return WinStatus.LOSE
        elif dealer_result == player_result:
            return WinStatus.DRAW

def get_dealer_turns(dealer_hand):
    while True:
        if(check_hand(dealer_hand)) >= 17:
            return check_hand(dealer_hand)
        else:
            create_turn(dealer_hand)

def fill_deck(deck):
    count = 0
    while True:
        deck.append(Card('2', 2, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('3', 3, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('4', 4, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('5', 5, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('6', 6, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('7', 7, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('8', 8, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('9', 9, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('10', 10, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('J', 10, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('Q', 10, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('K', 10, False))
        if count == 3:
            count = 0
            break
        else:
            count += 1
    while True:
        deck.append(Card('A', 11, False))
        if count == 3:
            break
        else:
            count += 1
    return deck

if __name__ == "__main__":
    deck = fill_deck([])
    random.shuffle(deck)
    name = input("Provide your name: ")
    value = int(input("Provide your balance: "))
    player = Player(name, value)
    dealer = Player("dealer", 100500)
    while True:
        result = ''
        bet= ''
        if player.balance <= 0:
            print("You lose")
            break
        else:
            bet = int(input("Make your bet"))
            if(player.balance - bet < 0):
                print("You haven't enough money")
                continue
            dealer_hand = Hand(dealer)
            player_hand = Hand(player)

            while True:
                if check_hand(player_hand) <= 21:
                    print(player_hand)
                    player_definition = input("Do you wanna another card? (y/n)")
                    if player_definition == 'y':
                        create_turn(player_hand)
                        print(dealer_hand)
                        print(player_hand)
                    elif player_definition == 'n':
                        result = finish_game(True, check_hand(player_hand), dealer_hand)
                        break
                    else:
                        continue
                else:
                    result = finish_game(False, check_hand(player_hand), dealer_hand)
                    print(dealer_hand)
                    print(player_hand)
                    break
        if result == WinStatus.WIN:
            player.balance += bet
        elif result == WinStatus.LOSE:
            player.balance -= bet

        print(result)
        print(player.balance)