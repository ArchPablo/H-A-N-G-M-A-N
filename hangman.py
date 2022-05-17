import random
import string

lost = 0
wins = 0
random.seed()
print('''H A N G M A N''')
while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    word_list = ('python', 'java', 'swift', 'javascript')
    word = random.choice(word_list)
    new_word = list(len(word) * '-')
    attempts = 8
    input_let = []
    if menu == 'results':
        print(f'You won: {wins} times')
        print(f'You lost: {lost} times')
    if menu == 'exit':
        break
    if menu == 'play':
        while True:
            new_s_word = ''.join(new_word)
            if attempts == 0:
                print('You lost!')
                lost += 1
                break
            if word == new_s_word:
                print(f'You guessed the word {word}!')
                print('You survived!')
                wins += 1
                break
            else:
                print('\n' + ''.join(new_word))
                letter = input('Input a letter:')
                if len(letter) != 1:
                    print('Please, input a single letter.')
                elif letter not in string.ascii_lowercase:
                    print('Please, enter a lowercase letter from the English alphabet.')
                elif letter in input_let and letter != "":
                    print("You've already guessed this letter")
                elif letter in word:
                    input_let.append(letter)
                    if letter in new_word:
                        attempts -= 1
                    else:
                        count = 0
                        for i in range(len(word)):
                            if letter == word[i]:
                                new_word[i] = letter
                else:
                    attempts -= 1
                    input_let.append(letter)
                    print("That letter doesn't appear in the word.")
    else:
        pass
