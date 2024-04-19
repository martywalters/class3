# A Student class with init method
class Student:

    def __init__(self, id, firstName, lastName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        if courses is 'None':
            self.courses = dict()
        else:
            self.courses = courses
        
    def __str__(self):
        course_str = ",".join(self.courses.keys())
        return f"{self.id:<6}  {self.lastName:<10}  {self.firstName:<8}   {self.gpa():.3f}    {course_str}"
    
    def __repr__(self):
        return f"{self.id},{self.lastName},{self.firstName},{self.courses}"

    def gpa(self):
        if not self.courses:
            return 0
        total_points = sum(self.courses.values())
        return total_points / len(self.courses)
    
    def addCourse(self, course, score):
        assert isinstance(score, (int, float)), "Score must be a numeric type"
        assert 0 <= score <= 4, "Score must be between 0 and 4"
        self.courses[course] = score
    
    def addCourses(self, courses):
         self.courses.update(courses)

    def header(self):
        return 'header'

    @classmethod
    def header(cls):
        return f"{'ID':<6}  {'Last Name':<10}  {'First Name':<8} {'GPA':<5}    Courses\n=========================================================================================="
        




student1 = Student(123456, "Johnnie", "Smith", {"CSE-101": 3.5, "CSE-102": 3, "CSE-201": 4, "CSE-220": 3.75, "CSE-325": 4})
student2 = Student(123457, "Sean", "Walters", {"CSE-101": 3.54})
print(Student.header())
print(student1)
print(student2)



    
