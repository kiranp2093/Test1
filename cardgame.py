import random

class Card:
    """A class to represent a playing card."""
    
    def __init__(self, value, suit):
        """
        Initialize a Card with a given value and suit.
        
        Args:
            value (int): The value of the card (2-14).
            suit (str): The suit of the card ("Clubs", "Diamonds", "Hearts", or "Spades").
        """
        self.suit = suit
        self.value = value
        self.name = self._get_card_name()

    def _get_card_name(self):
        """
        Get the name of the card based on its value.

        Returns:
            str: The name of the card.
        """
        if 2 <= self.value <= 10:
            return str(self.value)
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"
        elif self.value == 14:
            return "Ace"

    def __str__(self):
        """
        Return a string representation of the card.

        Returns:
            str: A string in the format "<name> of <suit>".
        """
        return f"{self.name} of {self.suit}"

class Deck:
    """A class to represent a standard deck of playing cards."""
    
    def __init__(self):
        """Initialize a standard deck of 52 cards and shuffle it."""
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):  # 2 to 14 (inclusive)
                self.cards.append(Card(value, suit))
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw a card from the deck. If the deck is empty, raise a RuntimeError.

        Returns:
            Card: The drawn card.
        """
        if not self.cards:
            raise RuntimeError("The deck is empty.")
        return self.cards.pop()