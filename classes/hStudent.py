from classes.hHuman import Human

# A subclass of Human that creates a Student object

class Student(Human):
    def __init__(self, profession="Unemployed Student") -> None:
        super().__init__(profession)

    def __setProfession(self, profession) -> None:
        return super().setProfession(profession)
