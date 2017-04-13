# Дыма Владимир. КНИТ16-А
# Cocktail shaker sort, Shellsort, Heapsort

import random as rn
import copy as c


def shake(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        for j in range(left, right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        right -= 1

        for j in range(right, left, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
        left += 1
    return arr


def shell(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            val, j = arr[i], i
            while j >= gap and arr[j-gap] > val:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = val
        gap //= 2
    return arr


def heap(arr):
    def heapify(last, j):
        '''Создаёт бинарное дерево.'''
        l = 2 * j + 1
        r = 2 * (j + 1)
        mx = j
        if l < last and arr[j] < arr[l]:
            mx = l
        if r < last and arr[mx] < arr[r]:
            mx = r
        if mx != j:
            arr[j], arr[mx] = arr[mx], arr[j]
            heapify(last, mx)

    end = len(arr)
    start = end // 2 - 1  # use // instead of /
    for k in range(start, -1, -1):
        heapify(end, k)
    for k in range(end - 1, 0, -1):
        arr[k], arr[0] = arr[0], arr[k]
        heapify(k, 0)
    return arr

N = int(input('Insert the length of the array: '))
A = rn.sample([i for i in range(-N + 1, N)], N)
B = c.deepcopy(A)
C = c.deepcopy(A)

print('Original array: \n{}'.format(A))
print('Cocktail shaker sort: \n{}'.format(shake(A)))
print('Shellsort: \n{}'.format(shell(B)))
print('Heapsort: \n{}'.format(heap(C)))
