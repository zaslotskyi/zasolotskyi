#1
def say_hi(name, age):
    if isinstance(name, str) and age >= 0:
        return f"Hi. My name is {name} and I'm {age} years old"
    else:
        print("First value(name) must me string \nSecond value(Age) must be int")

# print(say_hi("Ruslan", 10))


assert say_hi("Alex", 10) == "Hi. My name is Alex and I'm 10 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')


#2

def correct_sentence(text):
    if text[0].islower():
        text = text.capitalize()
        text_to_list = list(text)
        if text_to_list[-1] == ".":
            formatted_text = ''.join(text_to_list)
        else:
            text_to_list.append(".")
            formatted_text = ''.join(text_to_list)
        return formatted_text
    elif text[0].isupper():
        text_to_list = list(text)
        if text_to_list[-1] == ".":
            formatted_text = "".join(text_to_list)
        else:
            text_to_list.append(".")
            formatted_text = "".join(text_to_list)
        return formatted_text





assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')






