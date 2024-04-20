# Student class
from functools import reduce
class Student:

    def __init__(self, id, firstName, lastName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        if courses == None:
            self.courses = dict()
        else:
            self.courses = courses
        
    def __str__(self):
        course_str = ",".join(self.courses.keys())
        return f"{self.id:<6}    {self.lastName:<10}     {self.firstName:<8}       {self.gpa():.3f} {course_str}"
    
    def __repr__(self):
        return f"{self.id},{self.lastName},{self.firstName},{self.courses}"

    def gpa(self):
        if not self.courses:
            return 0
        #total_points = sum(self.courses.values())
        total_points = reduce(lambda x, y: x + y, self.courses.values()) #extra credit
        return total_points / len(self.courses)
    
    def addCourse(self, course, score):
        #assert isinstance(score, (int, float)), "Score must be a numeric type"
        #assert 0 <= score <= 4, "Score must be between 0 and 4"
        self.addCourses({course: score})
        
    
    def addCourses(self, courses):
        self.courses.update(courses)


    @classmethod
    def header(cls):
        return f"{'ID':<6}    {'Last Name':<10}     {'First Name':<8}       {'GPA':4}Courses\n"+'='*90
 
    #@staticmethod
    def printStudents(students):
        print(Student.header())
        for student in students:
            print(student)



print('\n' +'*'*15 + ' Part 1 '+ '*'*15 + '\n' )
student1 = Student(123456, "Johnnie", "Smith", {"CSE-101": 3.5, "CSE-102": 3, "CSE-201": 4, "CSE-220": 3.75, "CSE-325": 4})
student2 = Student(234567, "Jamie", "Strauss", {'CSE-101': 3.55, 'CSE-103': 3.45, 'CSE-202': 3.65, 'CSE-220': 3.35, 'CSE-401': 3.75})
student3 = Student(345678, "Jack", "O'Neill", {'CSE-101': 3.25, 'CSE-102': 3.15, 'CSE-103': 3.35, 'CSE-104': 3.25})


print(student1)
print(student2)
print(student3)

print()
print(repr(student1))
print()
print(Student.header())

# Creating students
students = [
    Student('123456', "Johnnie","Smith", {"CSE-101": 3.5, "CSE-102": 3.0, "CSE-201": 4.0, "CSE-220": 3.75, "CSE-325": 4.0}),
    Student('234567', "Jamie","Strauss", {"CSE-101": 3.0, "CSE-103": 3.5, "CSE-202": 3.25, "CSE-220": 4.0, "CSE-401": 4.0}),
    Student('345678', "Jack","O'Neill", {"CSE-101": 2.5, "CSE-102": 3.5, "CSE-103": 3.0, "CSE-104": 4.0}),
    Student('456789', "Susie","Marks"),
    Student('567890', "Frank","Marks"),
    Student('654321', "Annie","Marks"),
    #Student('456789', "Susie","Marks", {"CSE-101": 4.0, "CSE-103": 2.5, "CSE-301": 3.5, "CSE-302": 3.0, "CSE-310": 4.0}),
    #Student('567890', "Frank","Marks", {"CSE-102": 4.0, "CSE-104": 3.5, "CSE-201": 2.5, "CSE-202": 3.5, "CSE-203": 3.0}),
    #Student('654321', "Annie","Marks", {"CSE-101": 4.0, "CSE-102": 4.0, "CSE-103": 3.5, "CSE-201": 4.0, "CSE-203": 4.0}),
    Student('456987', "John","Smith", {"CSE-101": 2.5, "CSE-103": 3.0, "CSE-210": 3.5, "CSE-260": 4.0}),
    Student('987456', "Judy","Smith", {"CSE-102": 4.0, "CSE-103": 4.0, "CSE-201": 3.0, "CSE-210": 3.5, "CSE-310": 4.0}),
    Student('111354', "Kelly","Williams", {"CSE-101": 3.5, "CSE-102": 3.5, "CSE-201": 3.0, "CSE-202": 3.5, "CSE-203": 3.5}),
    Student('995511', "Brad","Williams", {"CSE-102": 3.0, "CSE-110": 3.5, "CSE-125": 3.5, "CSE-201": 4.0, "CSE-203": 3.0})
]
# Adding courses for students created without passing courses in __init__
students[3].addCourse("CSE-101", 4.0)
students[3].addCourse("CSE-103", 2.5)
students[3].addCourse("CSE-301", 3.5)
students[3].addCourse("CSE-302", 3.0)
students[3].addCourse("CSE-310", 4.0)

students[4].addCourse("CSE-102", 4.0)
students[4].addCourse("CSE-104", 3.5)
students[4].addCourse("CSE-201", 2.5)
students[4].addCourse("CSE-202", 3.5)
students[4].addCourse("CSE-203", 3.0)

students[5].addCourse("CSE-101", 4.0)
students[5].addCourse("CSE-102", 4.0)
students[5].addCourse("CSE-103", 3.5)
students[5].addCourse("CSE-201", 4.0)
students[5].addCourse("CSE-203", 4.0)
print('\n' +'*'*15 + ' Part 2 '+ '*'*15 +'\n' )
# Printing students
Student.printStudents(students)

print('\n' +'*'*15 + ' Part 3 '+ '*'*15 +'\n' )

# Query 1: Sort the list by lastName, firstName in ascending order
sorted_students_query1 = sorted(students, key=lambda x: (x.lastName, x.firstName))
print("Query 1: Sorted by last name, first name in ascending order")
Student.printStudents(sorted_students_query1)

# Query 2: Sort the list by GPA in descending order
sorted_students_query2 = sorted(students, key=lambda x: x.gpa(), reverse=True)
print("\nQuery 2: Sorted by GPA in descending order")
Student.printStudents(sorted_students_query2)

# Query 3: Create a set of unique courses taken by all students
unique_courses = {course for student in students for course in student.courses.keys()}
print("\nQuery 3: Unique courses taken by all students")
print(unique_courses)

# Query 4: Get a list of students who have taken 'CSE-201'
students_with_cse201 = [student for student in students if 'CSE-201' in student.courses]
print("\nQuery 4: Students who have taken 'CSE-201'")
Student.printStudents(students_with_cse201)

# Query 5: Get a list of honor roll students (GPA >= 3.5)
honor_roll_students = [student for student in students if student.gpa() >= 3.5]
print("\nQuery 5: Honor roll students (GPA >= 3.5)")
Student.printStudents(honor_roll_students)


#extra credit
# Query 3 with set comprehension
unique_courses_query3 = {course for student in students for course in student.courses}
print("\nQuery 3 with set comprehension: Unique courses taken by all students")
print(unique_courses_query3)



    
