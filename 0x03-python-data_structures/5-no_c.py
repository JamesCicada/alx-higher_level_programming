#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord(m): None for m in 'Cc'})
    return new
