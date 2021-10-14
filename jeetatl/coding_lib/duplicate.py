def get_duplicates(source_array):
    value_histogram = [0] * (len(source_array) + 1)
    duplicates = []

    for value in source_array:
        if value_histogram[value] == 1:
            duplicates.append(value)

        value_histogram[value] += 1

    return duplicates
