from domains.Student import Student
from domains.Course import Course
import input

cal1 = Course("MATH1.001", "Calculus 1", 4, ["BI034", "BA163", "BA478", "BI962", "BA728", "BI583"], [15.23, 13.98, 10.61, 5.19, 17.93, 18.32])
chem1 = Course("CHE1.001", "General chemistry 1", 4, ["BI583", "BA163", "BI034", "BA478", "BI962", "BA728"], [5.38, 6.91, 3.96, 7.53, 10.10, 11.32])
linear = Course("MATH1.002", "Linear algebra", 4, ["BA478", "BI962", "BA728", "BI034", "BI583", "BA163"], [12.19, 13.05, 8.51, 18.33, 13.67, 10.34]) 
gene = Course("BIO1.002", "Genetics", 3, ["BA728", "BI034", "BA478", "BI583", "BA163", "BI962"], [1.32, 9.24, 9.58, 3.23, 4.26, 1.68])
bp = Course("ICT1.002", "Basic programming", 4, ["BA163", "BA728", "BA478", "BI583", "BI034", "BI962"], [10.54, 10.54, 4.22, 15.89, 18.85, 9.58])   

list_course = input.add_list_course([cal1, bp, gene, linear, chem1])
for i in range(len(list_course)):
    input.input_mark(list_course[i])

cuong = Student("BA478", "Nguyen Van Cuong", "12/2/2001")
nam = Student("BI583", "Tran Van Nam", "5/1/2003")
an = Student("BA163", "Bat Binh An", "9/5/2005")
yen = Student("BA728", "Tan Ta Yen", "18/2/2000")
thuong = Student("BI962", "Dang Tinh Thuong", "2/1/1992")
alex = Student("BI034", "Alex Hwang", "30/9/1994")

list_student = input.add_list_student([cuong, nam, an, yen, thuong, alex])
for i in range(len(list_student)):
    input.find_mark(list_student[i])
    input.calculate_gpa(list_student[i])
list_student = sorted(list_student, key=lambda x: x.gpa, reverse = True)
