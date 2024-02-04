#1
def add_one(some_list):
    formatted_list_int = []
    some_list_to_int = int(''.join(map(str, some_list)))
    adding = some_list_to_int + 1
    formatted_list_str = list(str(adding))
    for item in range(len(formatted_list_str)):
        formatted_list_int.append(int(formatted_list_str[item]))
    return formatted_list_int


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


#2
def find_unique_value(some_list):
    new_list = [i for i in some_list if some_list.count(i) == 1]
    result = float(','.join(map(str, new_list)))
    return result




assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")


