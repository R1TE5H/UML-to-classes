from classes.hHuman import Human

class Teacher(Human):
    def __init__(self, profession="Unemployed Teacher") -> None:
        super().__init__(profession)

    def __setProfession(self, profession) -> None:
        return super().setProfession(profession)
