#Copy your practical work 1 to 2.student.mark.oop.py
#• Make it OOP’ed
#• Same functions
#   • Proper attributes and methods
#   • Proper encapsulation
#   • Proper polymorphism
#       • e.g. .input(), .list() methods

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.__mark = {}

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, value):
        self.__mark = value

    def input_mark(self, student_id, mark):
        current_mark = self.get_mark()
        for i in range(len(student_id)):
            current_mark[student_id[i]] = mark[i]
        self.set_mark(current_mark)

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse name: {self.course_name}\nMark: {self.__mark}"

class Student:
    def __init__(self, student_id, student_name, DoB):
        self.student_id = student_id
        self.student_name = student_name
        self.DoB = DoB
        self.__mark = {}

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, value):
        self.__mark = value

    def find_mark(self, list_course):
        for course in list_course:
            if self.student_id in course.get_mark():
                self.get_mark()[course.course_name] = course.get_mark()[self.student_id]
            self.set_mark(self.get_mark())

    def __str__(self):
        return f"Student ID: {self.student_id}\nStudent name: {self.student_name}\nDate of birth: {self.DoB}\nMark: {self.__mark}"

cal1 = Course("MATH1.001", "Calculus 1")
cal2 = Course("MATH1.003", "Calculus 2")
linear = Course("MATH1.002", "Linear algebra") 
list_course = [cal1, cal2, linear]  
list_course = sorted(list_course, key = lambda x: x.course_id)     

cal1.input_mark(["BA163", "BA478", "BI962", "BI583"], [15.2, 10.6, 5.1, 17.9])
cal2.input_mark(["BI583", "BA163", "BA478", "BI962"], [5.3, 3.9, 7.5, 10.1])
linear.input_mark(["BA478", "BI962", "BI583", "BA163"], [12.1, 8.5, 18.3, 10.3])

cuong = Student("BA478", "Cuong", "12/2/2001")
nam = Student("BI583", "Nam", "5/1/2003")
an = Student("BA163", "An", "9/5/2005")
thuong = Student("BI962", "Thuong", "2/1/1992")
list_student = [cuong, nam, an, thuong]
list_student = sorted(list_student, key=lambda x: x.student_name)

for i in range(len(list_student)):
    list_student[i].find_mark(list_course)

print("---------------------------------------------------------------------------------------------------------------------")
print("List courses:\n")
for i in range(len(list_course)):
    if i <= len(list_course)-2:
        print(list_course[i])
        print()
    else:
        print(list_course[i])
print("                        -----------------------------------------------------------------")
print("List students:\n")
for i in range(len(list_student)):
    if i <= len(list_student)-2:
        print(list_student[i])
        print()
    else:
        print(list_student[i])
print("---------------------------------------------------------------------------------------------------------------------")