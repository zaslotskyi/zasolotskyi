#1
first_number = int(input("Enter first number: "))
math_operation = input("Enter mathematical operation: ")
second_number = int(input("Enter second number "))
if math_operation == "/" and second_number == 0:
    print("You cannot divide by zero")
elif math_operation != "-" and math_operation != "+" and math_operation != "*" and math_operation != "/":
     print(f"{math_operation} is not a mathematical operation")
else:
    if math_operation == "*":
        result = first_number * second_number
    elif math_operation == "+":
        result = first_number + second_number
    elif math_operation == "-":
        result = first_number - second_number
    elif math_operation == "/" and second_number != 0:
        result = first_number / second_number
    print(result)

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


#2 best option
my_list = [12, 3, 4, 10]

if len(my_list) > 1:
    my_list.insert(0, my_list.pop())

print(my_list)



