#Functions
#• Input functions:
#    • Input number of students in a class
#    • Input student information: id, name, DoB
#    • Input number of courses
#    • Input course information: id, name
#    • Select a course, input marks for student in this course
#• Listing functions:
#    • List courses
#    • List students
#    • Show student marks for a given course


#    • Input number of students in a class
def n0_student(n0_student):
    return n0_student

#    • Input student information: id, name, DoB
list_student = []    
def student_in4(id, name, DoB):
    student = {
        "Student ID": id,
        "Student name": name,
        "Date of birth": DoB
    }
    if len(list_student) < n0_student(4):
        list_student.append(student)

#    • Input number of courses
def n0_course(n0_course):
    return n0_course

#    • Input course information: id, name
list_course = []
def course_in4(id, name):
    course = {
        "Course ID": id,
        "Course name": name,
    }
    if len(list_course) < n0_course(3):
        list_course.append(course)

#    • Select a course, input marks for student in this course
def input_mark(course_id, student_id, mark):
    for course in list_course:
        if course["Course ID"] == course_id:
            course["Mark"] = {}
            if len(student_id) != len(mark):
                return
            else:
                for j in range(len(student_id)):
                    course["Mark"][student_id[j]] = mark[j]

#    • Show student marks for a given course
def student_mark(student_id):
    for student in list_student:
        if student["Student ID"] == student_id:
            student["Mark"] = {}
            for course in list_course:
                if student_id in course["Mark"]:  
                    student["Mark"][course["Course name"]] = course["Mark"][student_id]


student_in4("BA478", "Cuong", "12/2/2001")
student_in4("BI583", "Nam", "5/1/2003")
student_in4("BA163", "An", "9/5/2005")
student_in4("BI962", "Thuong", "2/1/1992")
list_student = sorted(list_student, key=lambda x: x["Student name"])

course_in4("MATH1.001", "Calculus 1")
course_in4("MATH1.002", "Linear algebra")
course_in4("MATH1.003", "Calculus 2")

input_mark("MATH1.001", ["BA163", "BA478", "BI962", "BI583"], [15.2, 10.6, 5.1, 17.9])
input_mark("MATH1.002", ["BA478", "BI962", "BI583", "BA163"], [12.1, 8.5, 18.3, 10.3])
input_mark("MATH1.003", ["BI583", "BA163", "BA478", "BI962"], [5.3, 3.9, 7.5, 10.1])

student_mark("BA163")
student_mark("BA478")
student_mark("BI583")
student_mark("BI962")

print("---------------------------------------------------------------------------------------------------------------------")
print("List courses:")
for i in range(len(list_course)):
    print(list_course[i])
print("                        -----------------------------------------------------------------")
print("List students:")
for i in range(len(list_student)):
    print(list_student[i])
print("---------------------------------------------------------------------------------------------------------------------")