# index= open('namehere.html','w')
from random import sample


def four_digits():
    array = [x for x in range(10)]
    Array = sample(array, 4)
    # print(Array)
    if Array[0] == Array[1] or Array[1] == Array[2] or Array[3] == Array[1] or Array[3] == Array[0] or Array[3] == \
            Array[2] or Array[3] == Array[2]:
        return "error"
    else:
        return Array


def convert_input_to_array(inp):
    return [int(x) for x in str(inp)]


def check_input(inp, actual_input):
    final_arr = []
    number = ''
    for i in range(len(inp)):
        if inp[i] == actual_input[i]:
            final_arr.append(inp[i])
        else:
            final_arr.append("*")
    for elem in final_arr:
        number += str(elem)
    return number


# inp = input("Enter 4num digit: ")

# print(check_input(convert_input_to_array(inp), four_digits()))
# index.write(inp)
# index.close()