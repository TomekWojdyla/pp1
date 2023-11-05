#9.	A test is passed when the number of correctly completed tasks is at least 50%. Write a program that checks whether the test is passed. The total number of test tasks and the number of correctly completed tasks are included in variables. Sample result:

total_no = int(input("Now many tasks there were: "))
tasks_ok= int(input("now many tasks were done: "))
ratio=tasks_ok/total_no *100
if ratio >=50:
        print("Test passed")
else:
    print("Test failed")
