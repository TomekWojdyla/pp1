#30.	In a beverage factory, a machine fills 500ml bottles. The computer checks whether the bottle has been filled correctly. For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:
#508,500,512,499,492,511,503,476,501,509
##Write a program that calculates the percentage of incorrectly filled bottles. Use the filter() along with a higher order function. Sample result:
#Bottle capacity:    500ml
#Filling tolerance:  2%
#Filled bottles:     508,500,512,499,492,511,503,476,501,509
#Incorrectly filled: 30%

bottles = [508,500,512,499,492,511,503,476,501,509]

capacity = 500
perc = 2

def rate(val):
    def check(arr):
        check1 = list(filter(lambda x: x<(500+500*val*0.01) and x>(500-500*val*0.01),arr))
        new = 100-(len(check1)/len(arr)*100)
        return new
    return check 

test = rate(2)(bottles)
print(test)