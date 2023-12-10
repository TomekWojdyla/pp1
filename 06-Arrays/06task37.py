# 37.	Create a module MyArrays containing functions to operate on an array of numbers:
#a.	A function that returns the second largest element in an array
#b.	A function that returns the difference between the largest and smallest values in an array
#c.	A function that returns the median of numbers in an array. Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:
#https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png 
#d.	A function that returns a two-element array containing the smallest and largest values in an array
#e.	A function that returns array elements as a string, separated by the minus sign
#Then, write a program that for the sequence of numbers:
#7,3,8,5,2
#calculates and displays results. Sample result:
#Numbers: 7,3,8,5,2
#Second largest number: 7 
#Median: 5
#Smallest and largest number: 2,8

import MyArrays_tw

array1 = [7,3,8,5,2]
print(array1)
sec_lar = MyArrays_tw.second_largest(array1)
print(sec_lar)
diff_lar = MyArrays_tw.diff_lar(array1)
print(diff_lar)
#median1 = MyArrays_tw.arr_median(array1)
def arr_median1(arr):
    a = len(arr)//2
    value1 = arr[a]
    return value1
median1 = arr_median1(array1)
print(median1)

minmax = MyArrays_tw.min_max(array1)
print(minmax)

dashes = MyArrays_tw.array_as_string(array1)
print(dashes)