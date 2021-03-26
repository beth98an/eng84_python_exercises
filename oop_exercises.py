# OOP exercises

# Task 1: Fizz Buzz
class FizzBuzz():
    def __init__(self):
        self.fizz = "Fizz"
        self.buzz = "Buzz"
        self.fizzbuzz = "FizzBuzz"

    def fizz_buzz(self):
        for i in range(1, 100, 1):
            if i % 3 == 0 and i % 5 == 0:
                print(self.fizzbuzz)
            elif i % 5 == 0:
                print(self.buzz)
            elif i % 3 == 0:
                print(self.fizz)
            else:
                print(i)


fizz = FizzBuzz()
fizz.fizz_buzz()


# Task 2: Scrabble word calculator
class Scrabble():

    def __init__(self):
        self.scrab = {"A": 1, "B": 3, "C": 3, "D": 2,
                      "E": 1, "F": 4, "G": 2, "H": 4,
                      "I": 1, "J": 8, "K": 5, "L": 1,
                      "M": 3, "N": 1, "O": 1, "P": 3,
                      "Q": 10, "R": 1, "S": 1, "T": 1,
                      "U": 1, "V": 4, "W": 4, "X": 8,
                      "Y": 4, "Z": 10}
        self.string = input("What is your word? ")

    def scrabble_calc(self):
        value = 0
        word = self.string.upper()
        for i in word:
            if self.scrab[i]:
                value += self.scrab[i]
        return value


word_one = Scrabble()
print(word_one.scrabble_calc())

# Task 3: Naan Factory



