import random
class Hilo:
    """Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. 

    The responsibility of Hilo is to keep track of the card and calculate the points for it.
   
    Attributes:
        value (int): The value of the drawn card.
        points (int): The number of points the die is worth.
    """
    def __init__(self):
        """Constructs a new instance of Hilo with a value and points attribute.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value = random.randint(1,13)
        self.points = 0

    def card_draw(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value = random.randint(1,13)
        self.points = 0