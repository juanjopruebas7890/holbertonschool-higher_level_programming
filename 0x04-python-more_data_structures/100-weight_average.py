#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    q = 0.0
    list1 = list(i[0] * i[1] for i in my_list)
    list2 = list(i[1] for i in my_list)
    q = sum(list1) / sum(list2)
    return (q)
