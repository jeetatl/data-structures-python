def is_palindrome(input_string):
    start_index = 0
    end_index = len(input_string) - 1

    while end_index > start_index:
        if input_string[start_index] != input_string[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


if __name__ == '__main__':
    input_string = 'madam1'
    print("is %s a coding_lib? ", input_string)
    print(is_palindrome(input_string))
