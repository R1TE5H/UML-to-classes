# Class creating a Human object. 
# Each Human has an Profession variable

class Human:
    def __init__(self, profession="Unemployed Human") -> None:
        self.__setProfession(profession)

    def __setProfession(self, profession) -> None:
        self.__profession = profession

    def getProfession(self) -> str:
        return self.__profession
