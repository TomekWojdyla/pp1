# 33.	Write a program that creates a tuple containing single word ‘computation’. Save a tuple in a variable. Then, display the type of the variable.

test_tuple = ()
print(test_tuple)
print(type(test_tuple))

tuple_as_list = list(test_tuple)
tuple_as_list.append("computation")

print(tuple_as_list)
print(type(tuple_as_list))

test_tuple = tuple(tuple_as_list)
print(test_tuple)
print(type(test_tuple))