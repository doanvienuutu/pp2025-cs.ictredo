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

student_in4("BA478", "Minh", "12/2/2001")
student_in4("BI583", "Ngoc", "5/1/2003")
student_in4("BA163", "An", "9/5/2005")
student_in4("BI962", "Toan", "2/1/1992")
list_student = sorted(list_student, key=lambda x: x["Student name"])

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

course_in4("MATH1.001", "Calculus 1")
course_in4("MATH1.002", "Linear algebra")
course_in4("MATH1.003", "Calculus 2")

#    • Select a course, input marks for student in this course
def input_mark(i, id, mark):
    list_course[i]["Mark"] = {}
    if len(id) != len(mark):
        return
    else:
        for j in range(len(id)):
            list_course[i]["Mark"].update({id[j]: mark[j]})

input_mark(0, ["BA163", "BA478", "BI962", "BI583"], [15.2, 10.6, 5.1, 17.9])
input_mark(1, ["BA478", "BI962", "BI583", "BA163"], [12.1, 8.5, 18.3, 10.3])
input_mark(2, ["BI583", "BA163", "BA478", "BI962"], [5.3, 3.9, 7.5, 10.1])
print("List courses:")
for i in range(len(list_course)):
    print(list_course[i])


#    • Show student marks for a given course
list_student[0]["Mark"] = {       
        "MATH1.001 Calculus 1": list_course[0]["Mark"]["BA163"],
        "MATH1.002 Linear algebra": list_course[1]["Mark"]["BA163"],
        "MATH1.001 Calculus 2": list_course[2]["Mark"]["BA163"]
    }
list_student[1]["Mark"] = {
        "MATH1.001 Calculus 1": list_course[0]["Mark"]["BA478"],
        "MATH1.002 Linear algebra": list_course[1]["Mark"]["BA478"],
        "MATH1.001 Calculus 2": list_course[2]["Mark"]["BA478"]
    }
list_student[2]["Mark"] = {
        "MATH1.001 Calculus 1": list_course[0]["Mark"]["BI583"],
        "MATH1.002 Linear algebra": list_course[1]["Mark"]["BI583"],
        "MATH1.001 Calculus 2": list_course[2]["Mark"]["BI583"]
    }
list_student[3]["Mark"] = {
        "MATH1.001 Calculus 1": list_course[0]["Mark"]["BI962"],
        "MATH1.002 Linear algebra": list_course[1]["Mark"]["BI962"],
        "MATH1.001 Calculus 2": list_course[2]["Mark"]["BI962"]
    }
print("\nList students:")
for i in range(len(list_student)):
    print(list_student[i])