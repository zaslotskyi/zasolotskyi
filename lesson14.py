class TooManyStudentsError(Exception):
    def __init__(self, message="Too many students in the group!"):
        self.message = message
        super().__init__(self.message)


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



class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return
            else:
                print("There is no such student in this group")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student



    def __str__(self):
        all_students = ''
        for students in self.group:
            all_students += f'{str(students)}\n'
        return f"Group: {self.number}:\n{all_students}"






st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'
# gr.delete_student('Taylor')
# print(gr)  # Only one student
# gr.delete_student('Taylor')  # No error!
print(st2.compare_students(st1))