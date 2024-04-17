# A Student class with init method
class Student:

    def __init__(self, id, firstName, lastName, courses = None):
        self.firstName = firstName

    def gpa(self):
        return 0
    
    def addCourse(self, course, score):
        return 0
    
    def addCourses(self, courses):
        return 0

    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
    def header(self):
        return 'header'
        
    def say_hi(self):
        print('Hi ' + self.firstName)


s = Student(123,'Marty','Walters')
print(s)
s.say_hi()
    
