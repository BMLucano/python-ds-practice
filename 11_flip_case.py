def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_word= ""
    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            swapped_word += ltr.swapcase()
        else:
            swapped_word += ltr

    return swapped_word



