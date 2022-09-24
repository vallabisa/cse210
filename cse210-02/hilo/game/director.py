from game.hilo import Hilo
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        
        self.total_score = 300

        
      
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Hilo()
        while self.is_playing:
            
            self.previous_card = self.card.value
            print(f"\nThe card is: {self.previous_card}")
            self.do_updates()
            self.outputs()
            self.get_prompt()




    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        guess = input("Higher or lower? [h/l] ")
        self.card = Hilo()
        next_card = self.card.value
        print(f"Next card is: {next_card}")
        
        if guess == "h" and (next_card >= self.previous_card):
            self.total_score += 100
        elif guess == "l" and (next_card <= self.previous_card):
            self.total_score += 100
        else:
            self.total_score -= 75

        
       
        
    def outputs(self):
        """Displays the score. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}")

    def get_prompt(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """

        if self.total_score <= 0:
            self.is_playing = False
            print("Game over! Thank you for playing.")
        else:
            run_again = input("Play again? [y/n] ")
            self.is_playing = (run_again.lower() == "y")


