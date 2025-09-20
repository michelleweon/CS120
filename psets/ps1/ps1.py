from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """TODO: Implement Radix Sort using BC and singletonBucketSort"""

    n = len(arr)
    if n == 0:
        return []
    
    if univsize <= 1:
        k = 1
    else:
        k = int(math.ceil(math.log(univsize, base)))

    sorted_arr = []
    for K_i, V_i in arr:
        digits_i = BC(K_i, base, k)
        sorted_arr.append([0, (V_i, digits_i)])

    for j in range(k):
        for i in range(n):
            V_i, digits_i = sorted_arr[i][1]
            sorted_arr[i][0] = digits_i[j]
        sorted_arr = singletonBucketSort(base, sorted_arr)
    out = []
    for K_i, (Vi, digits_i) in sorted_arr:
        K_i = 0
        pow_b = 1
        for dj in digits_i:
            K_i += dj * pow_b
            pow_b *= base
        out.append([K_i, V_i])

    return sorted_arr