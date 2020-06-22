import enum
import random

class BlackJackConst():
    """
        Constants for BlackJack game
        LIMIT_POINT -> after this limit you lose the game
        ACE_DIFFERENCE -> Ace can be with value 1 and 11
        DEALER_TURN_LIMIT -> after this limit dealer stop draw
    """
    LIMIT_POINT = 21
    ACE_DIFFERENCE = 10
    DEALER_TURN_LIMIT = 17

class WinStatus(enum.Enum):
    """
        Define player win statuses
    """
    WIN = 1
    LOSE = 2
    DRAW = 3
    NOT_DEFINED = 4

class Player():
    """Class which defines player and drive player balance
    Args:
        name (str): provide a name of the player
        balance (int): provide a balance of the player
    """
    def __init__(self, name = "Default_name", balance = 0):
        self.name = name
        self.balance = balance

class Card():
    """Define a card for BlackJack game
    Args:
        name (str): provide a card name
        value (int): provide a card value to count a hand sum
        is_hidden (bool): property for display/hide a card name
    """
    def __init__(self, name = "", value = 0, is_hidden = False):
        self.name = name
        self.value = value
        self.is_hidden = is_hidden

    def __str__(self):
        return f"name : {self.name}, value: {self.value}"

class Deck():
    """Define a deck for BlackJack game"""
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

    def get_card(self) -> Card:
        """
        Returns:
            Card: return top card from the deck and remove it from deck
        """
        card = self.deck.pop()
        return card

    def fill_the_hand(self, is_hidden = False):
        """
        Args:
            is_hidden (bool): for first hidden card if it's a dealer
        :return: (Card[]) 2 start card for BlackJack game
        """
        first_card = self.deck.pop()
        if is_hidden:
            first_card.is_hidden = True
        result = [first_card, self.deck.pop()]
        return result

    def custom_deck_shuffle(self):
        """ Custom shuffle the deck for BlackJack game
        """
        for i in range(len(self.deck) - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i + 1)

            # Swap arr[i] with the element at random index
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

class Hand():
    """Define a player hand for BlackJack game
    Args:
        player (Player): Define a player
        deck (Deck): Provide a deck to BlackJack game
    """
    def __init__(self, player = Player(), deck = Deck()):
        self.player = player
        self.cards = deck.fill_the_hand(self)

    def __str__(self):
        result = f"{self.player.name}: "
        for card in self.cards:
            if card.is_hidden:
                result += ('* ')
            else:
                result += (card.name + ' ')
        return result