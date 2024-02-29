class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name} {self.first_name}, age: {self.age}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def compare_students(self, other_student):
        if self.age < other_student.age:
            return f'{self.last_name} {self.first_name} younger than {other_student.last_name} {other_student.first_name}'
        elif self.age > other_student.age:
            return f'{self.last_name} {self.first_name} older than {other_student.last_name} {other_student.first_name}'

    def __str__(self):
        return f'{self.last_name} {self.first_name}, age: {self.age}'