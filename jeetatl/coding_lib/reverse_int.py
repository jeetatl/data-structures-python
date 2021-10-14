import math


def reverse_int(input_integer):
    output_integer = input_integer % 10
    input_integer = math.floor(input_integer / 10)
    while input_integer > 0:
        output_integer *= 10
        output_integer += input_integer % 10
        input_integer = math.floor(input_integer / 10)
    return output_integer
