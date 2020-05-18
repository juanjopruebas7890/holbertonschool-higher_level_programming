#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tmp = 0
    while my_list and tmp < 0:
        print("{:d}".format(my_list[tmp]), end="")
        tmp += 1
    except (ValueError, TypeError):
        break
    print()
    return (tmp)
