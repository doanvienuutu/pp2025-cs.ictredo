import math, numpy as np
from domains.Course import Course

list_course = []
def add_list_course(x):
    global list_course
    for i in range(len(x)):
        list_course.append(x[i])
    list_course = sorted(list_course, key = lambda x: x.course_id)
    return list_course

def input_mark(x):
    current_mark = Course.get_mark(x)
    for i in range(len(x.list_student_id)):
        current_mark[x.list_student_id[i]] = math.floor(x.list_student_mark[i]*10) / 10 #• Use math module to round-down student scores to 1-digit decimal upon input, floor()
    return x.set_mark(current_mark)

list_student = []
def add_list_student(x):
    global list_student
    for i in range(len(x)):
        list_student.append(x[i])
    list_student = sorted(list_student, key=lambda x: x.gpa, reverse = True)
    return list_student    

def find_mark(x):
    global list_course
    for course in list_course:
        if x.student_id in course.get_mark(): #get_mark here belong to Course
            x.get_mark()[course.course_name] = course.get_mark()[x.student_id]
    return x.set_mark(x.get_mark())

def calculate_gpa(x):
    global list_course
    gp = np.array(list(x.get_mark().values()))
    etcs = np.array([i.etcs for i in list_course])
    gp_x_etcs = np.multiply(gp, etcs)
    numerator = np.sum(gp_x_etcs)
    denominator = np.sum(etcs)
    x.gpa = math.floor(numerator/denominator*10) / 10




