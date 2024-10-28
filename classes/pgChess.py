from classes.pgPairGame import PairGame

# A subclass of PairGame
# When playing, will print the players' professions, and
# that they are playing chess

class Chess(PairGame):
    def __init__(self, playerOne=None, playerTwo=None) -> None:
        super().__init__(playerOne, playerTwo)
    
    def play(self):
        print(f"Player One is a {self.getPlayerOne().getProfession()} and Player Two is a {self.getPlayerTwo().getProfession()}. \nThey are playing Chess together")
