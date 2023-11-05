#6.	Find out what the term “debugging” means. Then watch the video explaining how to test your program using the debugger.
#https://youtu.be/KEdq7gC_RTA 
#https://youtu.be/b4p-SBjHh28?feature=shared 

#7.	In the following program, mark breakpoints in lines 1, 5 and 7. Then, do the tasks below:
#a.	Run the program in debug mode. Then, execute all program statements, one by one. Observe the changing values of variables.
#b.	Run the program in debug mode. Move between the marked breakpoints.
#c.	Run the program in debug mode. Add the variable ‘sum’ and ‘number’ to the Watch window, and the expression number <= 5. Execute the program step by step. Observe the changes in the variables and in the added expression.

sum = 0
number = 1
while number <= 5:
  sum = sum + number
  number = number + 1
message = f"Sum of numbers in <1,5> is {sum}"
print(message)

