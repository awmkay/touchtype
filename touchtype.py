# Import correct modules
import sys
import os
import string
import re
import time

# Import functions from functions.py
import functions as fn

# Setup basic user variables
users = open('users.txt', 'r')
user = sys.argv[1]
word_list = open('word_list.txt', 'r')
word_list_specific = open('word_list_specific.txt', 'w')

# Find user in file and user letters
user_info = users.readline().split('\t')
user_info[1] = user_info[1].rstrip()
while user_info[0] != user:
    user_info = users.readline().split('\t')
    user_info[1] = user_info[1].rstrip()


# Search word list for words with specific letters and set word list
print(user_info[1])
fn.letter_check(user_info[1], word_list, word_list_specific)

# Check whether to start game
ready = input('Are you ready to start? (y / n) ').lower()
if ready != 'y':
    sys.exit()

# Game startup message
print('Starting in...')
for i in range(3):
    print(str(3 - i) + '...')
    time.sleep(1)
print('Start!')
