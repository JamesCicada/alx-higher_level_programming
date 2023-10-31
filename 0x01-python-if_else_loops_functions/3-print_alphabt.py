#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if letter not in 'qe':
        print("{}".format(chr(letter)), end='')
