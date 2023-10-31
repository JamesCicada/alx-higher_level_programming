#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if letter not 'q' and letter not 'e':
        print("{}".format(chr(letter)), end='')
