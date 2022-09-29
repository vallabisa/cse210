class Jumper:
    "This class is for every wrong guess"
    def __init__(self):
        
        self._lives = 4
        

    def display(self):
        file = open("Week5/Jumper Incompete/Text/Parachute.txt", "r")
        parachute = file.readlines()
        
        #parachute = ["  ___", "/ ___ \ ", "\     /", " \   /", "   O", "  /|\ ", "  / \ ", "⌃⌃⌃⌃⌃⌃⌃"]
        if self._lives == 4:
            for x in range(4-self._lives, len(parachute)):
                print(parachute[x])

        elif self._lives == 3:
            for x in range(4-self._lives, len(parachute)):
                print(parachute[x])

        elif self._lives == 2:
            for x in range(4-self._lives, len(parachute)):
                print(parachute[x])

        elif self._lives == 1:
            for x in range(4-self._lives, len(parachute)):
                print(parachute[x])

        elif self._lives == 0:
            for x in range(4-self._lives, len(parachute)):
                print(parachute[x])