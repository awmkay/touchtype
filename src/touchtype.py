# Import modules
import sys
import os
import string
import re
import time
import random

# Import functions from functions.py
import functions as fn

# Setup basic user variables
cwd = os.getcwd()

# Setup argv inputs
user = sys.argv[1]
num_words = int(sys.argv[2])

# Setup user files
users_file = open(os.path.join(
    cwd, '..', 'users', 'users.txt'), 'r')
timing = open(os.path.join(
    cwd, '..', 'users', user, 'timing.txt'), 'a')

# Setup word lists based on user info
word_list = open(os.path.join(
    cwd, '..', 'resources', 'word_list.txt'), 'r')
word_list_specific = open(os.path.join(
    cwd, '..', 'resources', 'word_list_specific.txt'), 'w')

# Find user in file and user letters
user_info = users_file.readline().split('\t')
user_info[1] = user_info[1].rstrip()
while user_info[0] != user:
    user_info = users_file.readline().split('\t')
    user_info[1] = user_info[1].rstrip()


# Search word list file for appropriate words and store in other file
fn.letter_check(user_info[1], word_list, word_list_specific)

# Write appropriate words to word list
words = fn.word_write(user_info[1], cwd, word_list_specific)

# Startup stuff
fn.startup()

# Start game
fn.game(words, timing, num_words)
