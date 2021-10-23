class DescendingFrequency:

    @staticmethod
    def frequency_sort(input_str: str) -> str:

        # the smallest character in dataset
        zero_ord = ord('0')

        # an array that saves the frequency of each character as it appears.
        char_frequency = [0] * 75

        for current_char in input_str:
            char_index = ord(current_char) - zero_ord
            char_frequency[char_index] += 1

        # create map of frequency to character
        frequency_char = dict()
        for index, value in enumerate(char_frequency):
            if value == 0:
                continue

            if frequency_char.get(value) is not None:
                frequency_char.get(value).append(index)
            else:
                frequency_char[value] = [index]

        sorted_frequency = list(frequency_char.keys())
        sorted_frequency.sort(reverse=True)
        sorted_string = ''

        for frequency in sorted_frequency:
            characters_with_frequency = frequency_char[frequency]
            for character in characters_with_frequency:
                sorted_string += (chr(character + zero_ord) * frequency)

        return sorted_string
