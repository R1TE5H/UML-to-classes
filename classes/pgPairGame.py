from classes.hHuman import Human

# A class creating a PairGame. 
# Has two parameters of type Human which can be set at instantiation
# ot later on 

class PairGame:

    def __init__(self, playerOne = None, playerTwo = None) -> None:
        self.setPlayerOne(playerOne)
        self.setPlayerTwo(playerTwo)

    def setPlayerOne(self, playerOne) -> None:
        self.__playerOne = playerOne

    def setPlayerTwo(self, playerTwo) -> None:
        self.__playerTwo = playerTwo

    def getPlayerOne(self) -> Human | None:
        return self.__playerOne
    
    def getPlayerTwo(self) -> Human | None:
        return self.__playerTwo
    
    def play(self):
        print(f"Player One is a {self.getPlayerOne().getProfession()} and Player Two is a {self.getPlayerTwo().getProfession()}")