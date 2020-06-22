import enum

class BlackJackConst():
    LIMIT_POINT = 21
    ACE_DIFFERENCE = 10
    DEALER_TURN_LIMIT = 17

class WinStatus(enum.Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3
    NOT_DEFINED = 4

class Player():

    def __init__(self, name = "Default_name", balance = 0):
        self.name = name
        self.balance = balance

class Card():

    def __init__(self, name = "", value = 0, is_hidden = False):
        self.name = name
        self.value = value
        self.is_hidden = is_hidden

    def __str__(self):
        return f"name : {self.name}, value: {self.value}"

class Deck():

    def __init__(self):
        self.deck = self.fill_deck()

    def fill_deck(self):
        deck = [Card('2' , 2),
                Card('3' , 3),
                Card('4' , 4),
                Card('5' , 5),
                Card('6' , 6),
                Card('7' , 7),
                Card('8' , 8),
                Card('9' , 9),
                Card('10', 10),
                Card('J' , 10),
                Card('Q' , 10),
                Card('K' , 10),
                Card('A' , 11)]
        deck = deck * 4
        return deck

    def get_card(self):
        card = self.deck.pop()
        return card

    def fill_the_hand(self, hand, is_hidden = False):
        first_card = self.deck.pop()
        if is_hidden:
            first_card.is_hidden = True
        result = [first_card]
        result.append(self.deck.pop())
        return result

class Hand():

    def __init__(self, player = Player(), deck = Deck(), is_dealer = False):
        self.player = player
        self.cards = deck.fill_the_hand(self, is_dealer)

    def __str__(self):
        result = f"{self.player.name}: "
        for card in self.cards:
            if card.is_hidden:
                result += ('* ')
            else:
                result += (card.name + ' ')
        return result