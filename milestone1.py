class Course:
    def __init__(self, course_code, credits, students):
        """initializes course object"""
        self.course_code = course_code
        self.credits = credits
        self.students = students

    def add_student(student):
        """Adds student to course roster"""

    def get_student_count():
        """returns number of student currently enrolled"""




class Student:
    def __init__(self, student_id, name, courses):
        """initializes student object"""
        self.student_id = student_id
        self.name = name
        self.courses = courses

    def enroll(course, grade):
        """enrolls student in course"""

    def update_grade(course, grade):
        """modifies student's grade in course"""

    def calculate_gpa():
        """calculates student's grade point average"""

    def get_courses():
        """returns list of courses taken by a student"""

    def get_course_info():
        """returns summary of all enrollements including: course code, grade, and credits""" 




class University:
    def __init__(self, students, courses):
        """initializes university object"""
        self.students = students
        self.courses = courses

    def add_course(course_code, credits):
        """creates new course if it does not already exist"""

    def add_student(student_id, name):
        """creates new student if it does not already exist"""

    def get_student(student_id):
        """returns student for given id"""

    def get_course(course_code):
        """returns course for given course code"""

    def get_course_enrollment(course_code):
        """returns number of student enrolled in a given course"""

    def get_students_in_course(course_code):
        """returns list of students in given course"""




GRADE_POINTS = {
'A' : 4.0, 'A-' : 3.7,
'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
'D' : 1.0,
'F' : 0.0
}