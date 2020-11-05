"""
Session 12 A
"""

class Student:
    __slots__ = ["name", "course_1", "course_2", "course_3", "course_4", "course_5"]
    def __init__ (self, name:str, course_1=None, course_2=None, course_3=None, course_4=None, course_5=None):
        self.name = name
        self.course_1 = course_1
        self.course_2 = course_2
        self.course_3 = course_3
        self.course_4 = course_4
        self.course_5 = course_5


class Course:
    __slots__ = ["name", "professor", "course_id", "meeting_time", "meeting_day"]
    def __init__ (self, name:str, professor:str, course_id:str, meeting_time:str, meeting_day:str):
        self.name = name
        self.professor = professor
        self.course_id = course_id
        self.meeting_time = meeting_time 
        self.meeting_day = meeting_day

def enroll(Student, Course):
    if Student.course_1 is None:
        Student.course_1 = Course
    elif Student.course_2 is None:
        Student.course_2 = Course
    elif Student.course_3 is None:
        Student.course_3 = Course
    elif Student.course_4 is None:
        Student.course_4 = Course
    elif Student.course_5 is None:
        Student.course_5 = Course
    else:
        print("Error, students can only enroll in 5 courses")

def main():
    s1 = Student('Name')
    c1 = Course(name = 'SE/CS', professor = 'Hamza', course_id = 'SWEC123', meeting_time = '4:00', meeting_day = 'Friday')

    enroll(s1, c1)
    print(s1.course_1.name)
if __name__ == "__main__":
    main()
