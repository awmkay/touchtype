import sys
import os
import string
import re
import time
import random


def letter_check(letters, word_list, word_list_specific):
    word = word_list.readline()
    while word:
        if re.match('^[{}]+$'.format(letters), word):
            word_list_specific.write(word)
        word = word_list.readline()
    word_list_specific.close()


def game(words, timing, num_words):
    # Set strings for startup
    typed = 'startup message'
    exit_str = 'exit()'

    # Start game
    while typed != exit_str:
        line = ' '.join(random.sample(words, num_words))
        print(line)

        # start timing
        t1 = float(time.time())
        typed = input().rstrip()

        # error checking
        while typed != line and typed != exit_str:
            print(line)
            typed = input().rstrip()

        # stop timing
        t2 = float(time.time())

        if typed != exit_str:
            # time calculations
            time_dif = float(t2 - t1)
            wpm = num_words * 60 / time_dif

            print(wpm)
            timing.write(str(wpm) + '\n')


def startup():
    # check whether user wants to play
    ready = input('Are you ready to start? (y / n): ').lower()
    if ready != 'y':
        sys.exit()

    # startup message
    print('Starting in...')
    for i in range(3):
        print(str(3 - i) + '...')
        time.sleep(1)
    print('Start!')
