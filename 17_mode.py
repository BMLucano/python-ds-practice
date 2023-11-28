def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    max = 0
    # counts{1: 2, 2: 1}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        # if(counts[num] > max):
        #     max = num
        max = num if counts[num] > max else max
    return max

