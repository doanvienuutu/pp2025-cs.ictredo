#• Copy your practical work 2 to 3.student.mark.oop.math.py
#• Use math module to round-down student scores to 1-digit
#  decimal upon input, floor()
#• Use numpy module and its array to
#   • Add function to calculate average GPA for a given student 
#   • Weighted sum of credits and marks
#   • Sort student list by GPA descending
#• Decorate your UI with curses module

import math, numpy as np, curses 
from curses import wrapper

class Course:
    def __init__(self, course_id, course_name, etcs):
        self.course_id = course_id
        self.course_name = course_name
        self.etcs = etcs
        self.__mark = {}

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, value):
        self.__mark = value

    def input_mark(self, student_id, mark):
        current_mark = self.get_mark()
        for i in range(len(student_id)):
            current_mark[student_id[i]] = math.floor(mark[i]*10) / 10 #• Use math module to round-down student scores to 1-digit decimal upon input, floor()
        self.set_mark(current_mark)

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse name: {self.course_name}\nETCS: {self.etcs}\nMark: {self.__mark}"
    
cal1 = Course("MATH1.001", "Calculus 1", 4)
chem1 = Course("CHE1.001", "General chemistry 2", 4)
linear = Course("MATH1.002", "Linear algebra", 4) 
gene = Course("BIO1.002", "Genetics", 3)
bp = Course("ICT1.002", "Basic programming", 4)
list_course = [cal1, chem1, linear, gene, bp]  
list_course = sorted(list_course, key = lambda x: x.course_id)     

cal1.input_mark(["BI034", "BA163", "BA478", "BI962", "BA728", "BI583"], [15.23, 13.98, 10.61, 5.19, 17.93, 18.32])
bp.input_mark(["BA163", "BA728", "BA478", "BI583", "BI034", "BI962"], [10.54, 10.54, 4.22, 15.89, 18.85, 9.58])
chem1.input_mark(["BI583", "BA163", "BI034", "BA478", "BI962", "BA728"], [5.38, 6.91, 3.96, 7.53, 10.10, 11.32])
gene.input_mark(["BA728", "BI034", "BA478", "BI583", "BA163", "BI962"], [1.32, 9.24, 9.58, 3.23, 4.26, 1.68])
linear.input_mark(["BA478", "BI962", "BA728", "BI034", "BI583", "BA163"], [12.19, 13.05, 8.51, 18.33, 13.67, 10.34])





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

    def find_mark(self, list_course):
        for course in list_course:
            if self.student_id in course.get_mark(): #get_mark here belong to Course
                self.get_mark()[course.course_name] = course.get_mark()[self.student_id]
            self.set_mark(self.get_mark())
    
    def calculate_gpa(self, list_course):
        gp = np.array(list(self.get_mark().values()))
        etcs = np.array([x.etcs for x in list_course])
        gp_x_etcs = np.multiply(gp, etcs)
        numerator = np.sum(gp_x_etcs)
        denominator = np.sum(etcs)
        self.gpa = math.floor(numerator/denominator*10) / 10

    def __str__(self):
        return f"Student ID: {self.student_id}\nStudent name: {self.student_name}\nDate of birth: {self.DoB}\nMark: {self.__mark}\nGPA: {self.gpa}"      

cuong = Student("BA478", "Nguyen Van Cuong", "12/2/2001")
nam = Student("BI583", "Tran Van Nam", "5/1/2003")
an = Student("BA163", "Bat Binh An", "9/5/2005")
yen = Student("BA728", "Tan Ta Yen", "18/2/2000")
thuong = Student("BI962", "Dang Tinh Thuong", "2/1/1992")
alex = Student("BI034", "Alex Hwang", "30/9/1994")
list_student = [cuong, alex, nam, an, thuong, yen]

for i in range(len(list_student)):
    list_student[i].find_mark(list_course)
    list_student[i].calculate_gpa(list_course)
list_student = sorted(list_student, key=lambda x: x.gpa, reverse = True)

#def ui(stdscr):
 #   curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
  #  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
   # YELLOW_AND_RED = curses.color_pair(1)
    #RED_AND_GREEN = curses.color_pair(2)
#    stdscr.addstr("---------------------------------------------------------------------------------------------------------------------")
 #   stdscr.addstr("List courses:\n", YELLOW_AND_RED)
print("---------------------------------------------------------------------------------------------------------------------")
print("List course:\n")
for i in range(len(list_course)):
    print(list_course[i])
    print()
  #  stdscr.addstr("                        -----------------------------------------------------------------")
   # stdscr.addstr("List students:\n", YELLOW_AND_RED)
print("                        -----------------------------------------------------------------")
print("List student:\n")
for i in range(len(list_student)):
    print(list_student[i])
    print()
print("---------------------------------------------------------------------------------------------------------------------")
#wrapper(ui)