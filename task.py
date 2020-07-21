import random
import re
import string


print("H A N G M A N")
letters = []
word = random.choice(['python', 'java', 'kotlin', 'javascript'])  # 'python'
letter_list = list(len(word) * "-")  # ----------
i = 8


class Game:

    def __init__(self, word, letter_list):
        self.word = word
        self.letter_list = letter_list
        self.i = 8
        self.letters = []

    def inadequate_input(self, letter):
        global letter_list
        if len(self.letter) != 1:
            print("You should input a single letter\n")
            print(''.join(self.letter_list))

        if self.letter not in string.ascii_lowercase and len(self.letter) == 1 and self.letter != "":
            print("It is not an ASCII lowercase letter\n")
            print(''.join(self.letter_list))
            self.letters.append(self.letter)

        if self.letter in self.letter_list or self.letter in self.letters and self.letter in string.ascii_lowercase and self.letter != "":
            print("You already typed this letter\n")
            print(''.join(self.letter_list))
            self.letters.append(self.letter)

        return

    def correct_letter(self):
        global letter_list
        if self.letter in self.word and self.letter != "" and self.letter not in self.letters and self.letter in string.ascii_lowercase:
            self.index_letter = [m.start() for m in re.finditer(self.letter, self.word)]  # генератор списка индексов елементов  [1, 3]
            for ind in self.index_letter:  # [1]
                letter_list[ind] = self.letter
                self.letters.append(self.letter)
            print("")
            print(''.join(self.letter_list))  # letter_list # ['-', 'a', '-', 'a']
            if "-" not in self.letter_list:  # проверка на то, законченное слово или нет.
                print("You guessed the word!\nYou survived!")
                self.i = 0

        return

    def wrong_letter(self):
        global letter_list
        if self.letter not in self.word and self.i != 1 and len(self.letter) == 1 and self.letter in string.ascii_lowercase and self.letter not in self.letters and self.letter != "":
            print("No such letter in the word\n")
            print(''.join(self.letter_list))
            self.i = self.i - 1
            self.letters.append(self.letter)
        elif self.letter not in self.word and self.i == 1 and len(self.letter) == 1 and self.letter in string.ascii_lowercase and self.letter not in self.letters and self.letter != "":
            print("No such letter in the word")
            print("You are hanged!")
            self.i = 0
            self.letters.append(self.letter)
        return

    def game_body(self):
        # status = input('Type "play" to play the game, "exit" to quit:')
        while self.i > 0:
            self.letter = input("Input a letter:")
            self.inadequate_input(self.letter)
            self.correct_letter()

            # self.index_letter = [m.start() for m in re.finditer(self.letter, self.word)]  # генератор списка индексов елементов  [1, 3]
            self.wrong_letter()


        # status = input('Type "play" to play the game, "exit" to quit:')


status = input('Type "play" to play the game, "exit" to quit:\n')
if status != "play" and status != "exit" or status == "":
    if len(status) != 1:
        print("You should input a single letter\n")

    elif status not in string.ascii_lowercase and status != "":
        print("It is not an ASCII lowercase letter\n")

while status == "play":
    letters = []
    word = random.choice(['python', 'java', 'kotlin', 'javascript'])  # 'python'
    letter_list = list(len(word) * "-")  # ----------
    i = 8
    print("")
    print(''.join(letter_list))
    hangman = Game(word, letter_list)
    hangman.game_body()
    print("")
    status = input('Type "play" to play the game, "exit" to quit:\n')
    if status != "play" and status != "exit" or status == "":
        if len(status) != 1:
            print("You should input a single letter\n")

        elif status not in string.ascii_lowercase and status != "":
            print("It is not an ASCII lowercase letter\n")