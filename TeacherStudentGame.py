# File to Run the Code

from classes.hTeacher import Teacher
from classes.hStudent import Student
from classes.pgChess import Chess
from classes.pgCheckers import Checkers

# Creating different Student and Teacher Instances 
student = Student("Software Engineer Student")
teacher = Teacher("Software Engineer")

student2 = Student("Computer Science Student")
teacher2 = Teacher("Computer Scientist")

# Instantiating Checkers and Chess Games with Initial Players
checkers = Checkers(student, teacher)
chess = Chess(student, teacher)

# Instantiating Checkers and Chess Games without Initial Players
checkers2 = Checkers()
chess2 = Chess()

# Setting the Checkers and Chess Players
checkers2.setPlayerOne(student2)
checkers2.setPlayerTwo(teacher2)

chess2.setPlayerOne(student2)
chess2.setPlayerTwo(teacher2)

# Playing Each Game
checkers.play()
chess.play()
