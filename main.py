# hangman
import random
import os
from data import word_list_full, stages

game_on = True
while game_on:
    def clear():
        os.system('cls')


    # choosing a word

    list_of_words = word_list_full
    word = random.choice(list_of_words)

    # defining variabels

    word_list = []

    for i in word:
        word_list += i

    word_list_deduct = word_list
    lives = len(word)
    gussing = ['_'] * len(word)
    mistake_num = 0
    form_display = 6

    while ' ' in word_list_deduct:
      i = word_list_deduct.index(' ')
      gussing = gussing[:i] + [' '] + gussing[i+1:]
      word_list_deduct = word_list_deduct[:i] + [''] + word_list_deduct[i+1:]


    # checking input

    while mistake_num < 6 and gussing != word_list:

        user_choice = input('pls guess a letter : ').lower()
        clear()

        if user_choice == ' ':
            print('space is not a letter!!!  ')

        elif user_choice in gussing:
            print(f'you already choosen {user_choice}')

        elif mistake_num == 5:
            print('you lost')
            print(stages[0])
            # Join all the elements in the list and turn it into a String.
            print(f"{' '.join(gussing)}")
            break


        elif user_choice not in word_list:
            mistake_num += 1
            form_display -= 1
            print(f'you lost 1 life for choosing {user_choice} remain {form_display}')

        elif gussing == word_list:
            print('you won')

        # finding multi letter
        while user_choice in word_list_deduct:
            i = word_list_deduct.index(user_choice)
            gussing = gussing[:i] + [user_choice] + gussing[i + 1:]
            word_list_deduct = word_list_deduct[:i] + [' '] + word_list_deduct[i + 1:]
            if gussing == word_list:
                print('you won')

        print(stages[form_display])
        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(gussing)}")
    print(f"\n{''.join(word_list)}".upper())

    game_stetus = input('press Y to play again or any key to exit... ').lower()
    if game_stetus != 'y':
        game_on = False

