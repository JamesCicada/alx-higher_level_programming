#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = []
    for i in my_list:
        found = False
        for item in result:
            if i == item:
                found = True
        if not found:
            result.append(i)
    print(result)
    return eval('+'.join(str(x) for x in result))

