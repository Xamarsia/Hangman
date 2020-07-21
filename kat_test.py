







import random
import re
import string

i = 8
print("H A N G M A N\n")
status = input('Type "play" to play the game, "exit" to quit:\n')
letters = []
word = random.choice(['python', 'java', 'kotlin', 'javascript'])  # 'python'
letter_list = list(len(word) * "-")  # ----------
print(''.join(letter_list))
if status == "play":
while i > 0:
    letter = input("Input a letter:")  # "p"
# .......................проверка на адекватний ввод ..................................
    if len(letter) != 1:
        print("You should input a single letter\n")
        print(''.join(letter_list))

    elif letter not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter\n")
        print(''.join(letter_list))

    elif letter in letter_list or letter in letters:
        print("You already typed this letter\n")
        print(''.join(letter_list))
# ........................ Правильная буква ..............................
    elif letter in word:
        index_letter = [m.start() for m in re.finditer(letter, word)]  # генератор списка индексов елементов  [1, 3]
        for ind in index_letter:  # [1]
            letter_list[ind] = letter
        print("")
        print(''.join(letter_list))  # letter_list # ['-', 'a', '-', 'a']
        if "-" not in letter_list:  # проверка на то, законченное слово или нет.
            print("""You guessed the word!
You survived!""")
            i = 0
# ........................ Неправильная буква ........................................
    else:
        if i != 1:
            print("No such letter in the word\n")
            print(''.join(letter_list))
            i -= 1
        else:
            print("No such letter in the word")
            print("You are hanged!")
            i -= 1
    letters.append(letter)
  # .............................................................................................
