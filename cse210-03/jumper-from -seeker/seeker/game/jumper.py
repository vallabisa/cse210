class Jumper:

    def __init__(self, ):
        self._alive = "O"
        self._line_1 = "  ___"
        self._line_2 = "/ ___ \ "
        self._line_3 = "\     /"
        self._line_4 = " \   /"
        self._line_5 = "   "
        self._line_6 = "  /|\ "
        self._line_7 = "  / \ "
        self._line_8 = "⌃⌃⌃⌃⌃⌃⌃"


    def get_alive(self):
        self._alive = "x"

    def display(self, number):
        self.check = number
        if self.check == 4:
            print(self._line_1)
            print(self._line_2)
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 3:
            print(self._line_2)
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 2:
            print(self._line_3)
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 1:
            print(self._line_4)
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)
        if self.check == 0:
            self.get_alive()
            print(self._line_5 + self._alive)
            print(self._line_6)
            print(self._line_7)
            print("")
            print(self._line_8)

    def update(self):
        return 1



# import random

# class Hider:
#     """The person hiding from the Seeker. 
    
#     The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
#     Attributes:
#         _location (int): The location of the hider (1-1000).
#         _distance (List[int]): The distance from the seeker.
#     """

#     def __init__(self):
#         """Constructs a new Hider.

#         Args:
#             self (Hider): An instance of Hider.
#         """
#         self._location = random.randint(1, 1000)
#         self._distance = [0, 0] # start with two so get_hint always works
    
#     def get_hint(self):
#         """Gets a hint for the seeker.

#         Args:
#             self (Hider): An instance of Hider.
        
#         Returns:
#             string: A hint for the seeker.
#         """
#         hint = "(-.-) Nap time."
#         if self._distance[-1] == 0:
#             hint = "(;.;) You found me!"
#         elif self._distance[-1] > self._distance[-2]:
#             hint = "(^.^) Getting colder!"
#         elif self._distance[-1] < self._distance[-2]:
#             hint = "(>.<) Getting warmer!"
#         return hint

#     def is_found(self):
#         """Whether or not the hider has been found.

#         Args:
#             self (Hider): An instance of Hider.
            
#         Returns:
#             boolean: True if the hider was found; false if otherwise.
#         """
#         return (self._distance[-1] == 0)
        
#     def watch_seeker(self, seeker):
#         """Watches the seeker by keeping track of how far away it is.

#         Args:
#             self (Hider): An instance of Hider.
#         """
#         distance = abs(self._location - seeker.get_location())
#         self._distance.append(distance)