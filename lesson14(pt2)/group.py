class TooManyStudentsError(Exception):
    def __init__(self, message="Too many students in the group!"):
        self.message = message
        super().__init__(self.message)


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