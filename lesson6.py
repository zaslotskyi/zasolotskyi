#1
my_list = [{"name": "John", "age": 33},
           {"name": "Jack", "age": 45},
           {"name": "Roman", "age": 15},
           {"name": "Ruslan", "age": 25},
           {"name": "Anton", "age": 30},
           {"name": "Vlad", "age": 15}
           ]
youngest_person = []
age = []
names = []
list_of_longest_names = []
avarage_age = []
for item in my_list:
    names.append(item["name"])
    age.append(item["age"])
sorted_age = sorted(age)
for i in range(len(sorted_age)):
    if sorted_age[i] <= sorted_age[0]:
        youngest_person.append(sorted_age[i])
print("List of youngest person:", youngest_person)

for i in range(len(names)):
    longest_name = max(names, key=len)
    if len(names[i]) == len(longest_name):
        list_of_longest_names.append(names[i])
print("List of longest names:", list_of_longest_names)

avarage_age = sum(age) / len(age)
print("Avarage ages:", avarage_age)


#2
first_dict = {
    "name": "Ruslan",
    "age": 26,
    "phone_number": "380670010001"
}
second_dict = {
    "surname": "Zaslotskyi",
    "age": 26,
    "phone_number": "380670020002"
}

first_dict_to_set = set(first_dict)
second_dict_to_set = set(second_dict)
print("A list of keys that are in the first dictionary but not in the second dictionary: ", list(first_dict_to_set.difference(second_dict_to_set)),
      "\nA list of keys that are in both dictionaries: ", list(first_dict_to_set.intersection(second_dict_to_set)))


third_dict = dict(item for item in first_dict.items() if item[0] not in second_dict)
print("A dictionary with a key and value which not in the second dictionary: ",third_dict)


com_keys = first_dict.keys() & second_dict
third_dict = first_dict.copy()
third_dict.update(second_dict)
third_dict.update({key: [first_dict[key], second_dict[key]] for key in com_keys})
print("United dictionaries: ", third_dict)












