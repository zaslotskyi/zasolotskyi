import keyword
import string
#1

value = (input("Enter value: "))
def can_be_value(value):
    reserved = keyword.kwlist
    spec_char = [i for i in list(string.punctuation) if i != "_"]
    if not value[0].isnumeric():
        if not value in reserved:
            for symbols in value:
                if symbols in spec_char or symbols.isupper() or "__" in value or " " in value:
                    return False
            return True
    return False

print(can_be_value(value))



#2


# while True:
#     first_number = int(input("Enter first number: "))
#     math_operation = input("Enter mathematical operation: ")
#     second_number = int(input("Enter second number "))
#     if math_operation == "/" and second_number == 0:
#         print("You cannot divide by zero")
#     elif math_operation != "-" and math_operation != "+" and math_operation != "*" and math_operation != "/":
#         print(f"{math_operation} is not a mathematical operation")
#     else:
#         if math_operation == "*":
#             result = first_number * second_number
#         elif math_operation == "+":
#             result = first_number + second_number
#         elif math_operation == "-":
#             result = first_number - second_number
#         elif math_operation == "/" and second_number != 0:
#             result = first_number / second_number
#         print(result)
#     repeat = input("Do you want continue?(yes/no): ")
#     if repeat == "yes":
#         continue
#     elif repeat == "no":
#         break
#     else:
#         break










