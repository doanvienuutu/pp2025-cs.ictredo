class Student:
    def __init__(self, student_id, student_name, DoB):
        self.student_id = student_id
        self.student_name = student_name
        self.DoB = DoB
        self.__mark = {}
        self.gpa = 0

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, value):
        self.__mark = value

    def __str__(self):
        return f"Student ID: {self.student_id}\nStudent name: {self.student_name}\nDate of birth: {self.DoB}\nMark: {self.__mark}\nGPA: {self.gpa}"      