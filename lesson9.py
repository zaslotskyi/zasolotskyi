#1
def popular_words(text, words):
    word_list = text.lower().split()
    word_counts = {word: 0 for word in words}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
    return word_counts

assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
#це було складно)) я перше хотів через каунтер зробити, але він не виводив 'three': 0, 'near': 0. Я походу прочитав усі треди на стаковерфлоу, які тільки існують)

2
def difference(*args):
    if args:
        my_list = list(args)
        max_value = max(my_list)
        min_value = min(my_list)
        sub = max_value - min_value
        return round(sub, 2)
    else:
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

