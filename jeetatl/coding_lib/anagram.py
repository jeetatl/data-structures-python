def is_anagram(source, target):
    source_histogram = [0] * 26

    for letter in source:
        source_histogram[(ord(letter) - ord("a"))] += 1

    for letter in target:
        source_histogram[(ord(letter) - ord("a"))] -= 1

    for value in source_histogram:
        if value != 0:
            return False

    return True
