#Write a function my_sort which takes in a list of numbers (positive integers).
#The function should return a list of sorted numbers such that odd numbers come first and even numbers come last.

#For example:
#my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) => [1, 3, 5, 7, 9, 2, 4, 6, 8]
#my_sort([1, 2]) => [1, 2]
#my_sort([2, 1]) => [1, 2]
#my_sort([3, 3, 4]) => [3, 3, 4]
#my_sort([90, 45, 66]) => [45, 66, 90]


def my_sort(number):
    even = [n for n in number if n % 2 == 0]
    odd = [n for n in number if n % 2 != 0]
    return sorted(odd) + sorted(even)
print(my_sort([2,4,5]))
print(my_sort([2,4,5,9]))



