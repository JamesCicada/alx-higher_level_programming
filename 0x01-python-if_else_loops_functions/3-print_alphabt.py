#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if letter != 'q' and letter != 'e':
        print("{}".format(chr(letter)), end='')
