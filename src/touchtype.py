# Import correct modules
import sys
import os
import string
import re
import time
import random
import colorama

# Import functions from functions.py
import functions as fn

# Setup basic user variables
cwd = os.getcwd()

# Setup user info/files
user = sys.argv[1]
num_words = int(sys.argv[2])
users = open('users.txt', 'r')
timing = open(os.path.join(cwd, user, 'timing.txt'), 'a')

# Setup word lists based on user info
word_list = open('word_list.txt', 'r')
word_list_specific = open('word_list_specific.txt', 'w')

# Find user in file and user letters
user_info = users.readline().split('\t')
user_info[1] = user_info[1].rstrip()
while user_info[0] != user:
    user_info = users.readline().split('\t')
    user_info[1] = user_info[1].rstrip()


# Search word list for appropriate words
fn.letter_check(user_info[1], word_list, word_list_specific)
word_list_specific = open('word_list_specific.txt', 'r')
words = word_list_specific.read().splitlines()

# Check whether to start game
ready = input('Are you ready to start? (y / n): ').lower()
if ready != 'y':
    sys.exit()

# Startup Message
print('Starting in...')
for i in range(3):
    print(str(3 - i) + '...')
    time.sleep(1)
print('Start!')

# Start game
fn.game(words, timing, num_words)
