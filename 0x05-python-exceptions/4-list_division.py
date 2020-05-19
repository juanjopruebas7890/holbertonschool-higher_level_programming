#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    for q in range(0, list_length):
        try:
            i = my_list_1[q] / my_list_2[q]
        except (ValueError, TypeError):
            print('wrong type')
            i = 0
        except (ZeroDivisionError):
            print('division by 0')
            i = 0
        except (IndexError):
            print('out of range')
            i = 0
        finally:
            l.append(i)
    return (l)
