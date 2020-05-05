#!/usr/bin/python3
def no_c(my_string):
        f = ''
        for i in my_string:
                if i == 'c' or i == 'C':
                        continue
                else:
                        f = f + i
        return (f)
