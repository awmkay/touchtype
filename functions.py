import re


def letter_check(letters, word_list, word_list_specific):
    word = word_list.readline()
    while word:
        if re.match('^[{}]+$'.format(letters), word):
            word_list_specific.write(word)
        word = word_list.readline()
