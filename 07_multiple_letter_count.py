def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_counts = {}

    # for ltr in phrase:
    #     if (ltr in letter_counts):
    #         letter_counts[ltr] += 1
    #     else:
    #         letter_counts[ltr] = 1

    for ltr in phrase:
        letter_counts[ltr] = letter_counts.get(ltr, 0) + 1

    return letter_counts

# get method
