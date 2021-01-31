"""
Name: Arthur Vico
PID: A58261993
"""

def quick_sort(unsorted, threshold, start, end, reverse=False):
    """
    This function will perform quick sort on the given list within the given range of indices while
    the length of that list is greater than the given threshold. Once the size of the given range of
    indices is equal to or less than the
    given threshold insertion sort will be used.
    :param unsorted: A python list that will be sorted by this function
    :param threshold: The maximum length that the list can be in order for insertion sort to be
    called instead of quick sort
    :param start: the start index of the range of values in the list that the function is working
    with
    :param end: The end index of the range of value in the list that the function is working with
    :param reverse: Defaults to False is no value is supplied. If the reverse value is False
    then the list will be sorted in increasing order (from smallest to largest). If the reverse
    value is True then the list will be sorted in decreasing order (from largest to smallest).
    :return: None, this function will sort the list in place
    """
    if threshold > end:
        insertion_sort(unsorted, start, end, reverse)
    elif start > end:
        return threshold
    else:
        divide = subdivide(unsorted, start, end, reverse)
        quick_sort(unsorted, threshold, start, divide - 1, reverse)
        quick_sort(unsorted, threshold, divide + 1, end, reverse)

def subdivide(unsorted, start, end, reverse):
    """
    This function will perform subdivide on the given list within the range of given indices.
    :param unsorted: A python list that will be used by this function
    :param start: the start index of the range of values in the list that the function
    is working with
    :param end: The end index of the range of value in the list that the function is working with
    :param reverse:If the reverse value is False then the list will be sorted in increasing order
    (from smallest to largest). If the reverse value is True then the list will be sorted in
    decreasing order (from largest to smallest).
    :return: The index of where the pivot ends up in the list
    """
    pivot = find_pivot(unsorted, start, end)
    left = start
    right = end-1
    if not reverse:
        #This code was taken from Onsay
        while left <= right:
            while left <= right and unsorted[left] < pivot:
                left += 1
            while left <= right and pivot < unsorted[right]:
                right -= 1
            if left <= right:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                left, right = left + 1, right - 1
        unsorted[left], unsorted[end] = unsorted[end], unsorted[left]

    else:
        while left <= right:
            while left <= right and unsorted[left] > pivot:
                left += 1
            while left <= right and pivot > unsorted[right]:
                right -= 1
            if left <= right:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                left, right = left + 1, right - 1
        unsorted[left], unsorted[end] = unsorted[end], unsorted[left]
    return left


def find_pivot(unsorted, start, end):
    """
    This function will use a median of three in order to find the pivot
    value for the given range of indices.
    :param unsorted: A python list that will be used by this function
    :param start: the start of the range of values in the list that the function is working with
    :param end: The end of the range of value in the list that the function is working with
    :return: The value of the pivot
    """
    mid = (end+start) // 2
    if unsorted[start] > unsorted[end]:
        unsorted[end], unsorted[start] = unsorted[start], unsorted[end]
    if unsorted[start] > unsorted[mid]:
        unsorted[mid], unsorted[start] = unsorted[start], unsorted[mid]
    if unsorted[end] < unsorted[mid]:
        unsorted[mid], unsorted[end] = unsorted[end], unsorted[mid]
    unsorted[mid], unsorted[end] = unsorted[end], unsorted[mid]
    # this is repetitive but I had first implemented my code so that pivot would be in the middle.
    # I have found out that it would be easier to have it at the end.
    return unsorted[end]

def insertion_sort(unsorted, start, end, reverse):
    """
    This function will perform insertion sort in-place on the given list
    within the given range of indices.
    :param unsorted: A python list that will be sorted by this function
    :param start: the start of the range of values in the list that the function is working with
    :param end: The end of the range of value in the list that the function is working with
    :param reverse: If the reverse value is False then the list will be sorted in increasing order
    (from smallest to largest). If the reverse value is True then the list will be sorted
    in decreasing order (from largest to smallest).
    :return: None, this function will sort in place
    """

    for i in range(1, len(unsorted)):
        current = unsorted[i]
        j = i-1
        if not reverse:
            while j >= 0 and current < unsorted[j]:
                unsorted[j+1] = unsorted[j]
                j -= 1
        if reverse:
            while j >= 0 and current > unsorted[j]:
                unsorted[j+1] = unsorted[j]
                j -= 1
        unsorted[j+1] = current




def largest_sequential_difference(lst):
    """
    This function will find the largest difference between sequential values in a sorted list
    using the given list.
    :param lst: A python list that will be used to find the largest sequential difference
    :return:An integer that is the largest difference between sequential numbers. Unless the
    length of the list is less than 2, then None will be returned.
    """
    quick_sort(lst, 0, 0, len(lst)-1, False)
    max = 0
    if len(lst) < 2:
        return None
    for i in range(len(lst)-1):
        if i <= (len(lst)-2):
            if lst[i+1] - lst[i] > max:
                max = lst[i+1] - lst[i]
    return max
