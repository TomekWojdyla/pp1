#21.	Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:
#a.	Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
#b.	Display all numbers separated by a space
#c.	Determine the greatest number
#d.	Determine the smallest number
#e.	Calculate the arithmetic mean of numbers
#f.	Calculate of the median
#.	Display of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)
#hen, use the program for numbers:
#12, 37, 6, 9, 17 

import statistics

class Mystatistics():
    def __init__(self):
        self.numbers = []
        self.min = 0
        self.max = 0
        self.artmean = 0
        self.med = 0
    def add_numbers(self):
        check = False
        while check == False:
            new = input("Enter new set number: ")
            if new !="":
                self.numbers.append(int(new))
            else:
                check = True
    def maximum(self):
        self.max = max(self.numbers)
    def mminimum(self):
        self.min = min(self.numbers)
    def median(self):
        self.med = statistics.median(self.numbers)
    def art_mean(self):
        sum = 0
        for i in range (len(self.numbers)):
            sum += self.numbers[i]
        self.artmean = sum/len(self.numbers)
    def __str__(self):
        return "Max: " + str(self.max) + "Min: " + str(self.min) + "Med: " + str(self.artmean) +"Median: "+ str(self.med)
    
Myarr = Mystatistics()
Myarr.add_numbers()
Myarr.maximum()
Myarr.mminimum()
Myarr.median()
Myarr.art_mean()
print(Myarr)