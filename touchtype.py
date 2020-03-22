# Import correct modules
import sys
import os
import string
import re


def letter_check(letters, word_list, word_list_specific):
    word = word_list.readline()
    while word:
        if re.match('^[{}]+$'.format(letters), word):
            word_list_specific.write(word)
        word = word_list.readline()


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


# Search word list for words with specific letters
print(user_info[1])
letter_check(user_info[1], word_list, word_list_specific)
