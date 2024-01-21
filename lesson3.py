#1
first_number = int(input("Enter first number: "))
math_operation = input("Enter mathematical operation: ")
second_number = int(input("Enter second number "))
if math_operation == "*":
    multiplication = first_number * second_number
    print(multiplication)
elif math_operation == "+":
    addition = first_number + second_number
    print(addition)
elif math_operation == "-":
    subtraction = first_number - second_number
    print(subtraction)
elif math_operation == "/" and second_number != 0:
    division = first_number / second_number
    print(round(division))
else:
    print("You cannot divide by zero")

#2
my_list = [12, 3, 4, 10]
if len(my_list) != 0:
    second_list = my_list.copy()
    last_element = second_list[-1]
    relocate_last_element = second_list.insert(0, last_element)
    delete_last_element = second_list.pop()
    print(second_list)
else:
    print(my_list)



