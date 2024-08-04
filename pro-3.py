class SaurastraUniversity:
    def __init__(self, university_name):
        self.university_name = university_name
    def display_university_info(self):
        print(f"University Name: {self.university_name}")

class TnraoCollege(SaurastraUniversity):
    def __init__(self, university_name, college_name):
        super().__init__(university_name)
        self.college_name = college_name
    def display_college_info(self):
        print(f"College Name: {self.college_name}")

class Student(TnraoCollege):
    def __init__(self, university_name, college_name, student_name, roll_no):
        super().__init__(university_name, college_name)
        self.student_name = student_name
        self.roll_no = roll_no
    def display_student_info(self):
        print(f"Student Name: {self.student_name}")
        print(f"Roll No: {self.roll_no}")
student = Student("Saurastra University", "TN Rao College", "Rajesh", 101)
student.display_university_info()
student.display_college_info()
student.display_student_info()
