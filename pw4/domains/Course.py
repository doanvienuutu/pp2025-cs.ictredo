class Course:
    def __init__(self, course_id, course_name, etcs, list_student_id, list_student_mark):
        self.course_id = course_id
        self.course_name = course_name
        self.etcs = etcs
        self.list_student_id = list_student_id
        self.list_student_mark = list_student_mark
        self.__mark = {}

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, value):
        self.__mark = value

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse name: {self.course_name}\nETCS: {self.etcs}\nMark: {self.__mark}"
