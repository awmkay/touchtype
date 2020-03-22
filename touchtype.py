# Import correct modules
import sys
import os
import string
import re

# Setup basic user variables
users = open('users.txt', 'r')
user = sys.argv[1]

# Find user in file and user letters
user_info = users.readline().split('\t')
user_info[1] = user_info[1].rstrip()
while user_info[0] != user:
    user_info = users.readline().split('\t')
    user_info[1] = user_info[1].rstrip()

# Search word list for words with specific letters
