import random

class Puzzle:

    def __init__(self):
        self._word_list = ["puzzle","jumper"]
        self._word_selected = ""

        self._word_guess = ["_ "] * len(self._word_selected)

    
    def _select_word(self):
        #self._word_selected = 
        pass

    def draw_word_guess(self):
        pass

    def process_guess(self, guess_letter):
        pass

    def can_keep_guessing(self):
        pass


# # TODO: Implement the Seeker class as follows...
# import random
# # 1) Add the class declaration. Use the following class comment.

# class Seeker:
#     """The person looking for the Hider. 
    
#     The responsibility of a Seeker is to keep track of its location and distance travelled.
    
#     Attributes:
#         location (int): The location of the Seeker (1-1000).
#     """

# # 2) Create the class constructor. Use the following method comment.
#     def __init__(self):
#         """Constructs a new Seeker.

#         Args:
#             self (Seeker): An instance of Seeker.
#         """
#         self._location = random.randint(1,1000)
       
# # 3) Create the get_location(self) method. Use the following method comment.
#     def get_location(self):
#         """Gets the current location.
        
#         Returns:
#             number: The current location,
#         """
#         return self._location
        
# # 4) Create the move_location(self, location) method. Use the following method comment.
#     def move_location(self, location):
#         """Moves to the given location.

#         Args:
#             self (Seeker): An instance of Seeker.
#             location (int): The given location.
#         """
#         self._location = location