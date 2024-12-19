
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id, course):
        Person.__init__(self, name, age, address)
        self.student_id = student_id
        self.course = course

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}, Course: {self.course}")


class Staff(Person):
    def __init__(self, name, age, address, staff_id, position):
        Person.__init__(self, name, age, address)
        self.staff_id = staff_id
        self.position = position

    def display_staff_info(self):
        self.display_person_info()
        print(f"Staff ID: {self.staff_id}, Position: {self.position}")


class TeachingStaff(Staff):
    def __init__(self, name, age, address, staff_id, position, subject, department):
        Staff.__init__(self, name, age, address, staff_id, position)
        self.subject = subject
        self.department = department

    def display_teaching_staff_info(self):
        self.display_staff_info()
        print(f"Subject: {self.subject}, Department: {self.department}")


class ResearchStudent(Student, TeachingStaff):
    def __init__(self, name, age, address, student_id, course, staff_id, position, subject, department, research_topic):
        Student.__init__(self, name, age, address, student_id, course)
        TeachingStaff.__init__(self, name, age, address, staff_id, position, subject, department)
        self.research_topic = research_topic

    def display_research_student_info(self):
        self.display_student_info()
        print(f"Staff ID: {self.staff_id}, Position: {self.position}, Subject: {self.subject}, Department: {self.department}")
        print(f"Research Topic: {self.research_topic}")


student = Student("Alice", 20, "123 University Ave", "S1234", "Computer Science")
student.display_student_info()

print("")

teaching_staff = TeachingStaff("Dr. Bob", 45, "456 Faculty Rd", "T5678", "Professor", "Physics", "Science")
teaching_staff.display_teaching_staff_info()

print("")

research_student = ResearchStudent(
    name="Charlie", age=28, address="789 Research Blvd",
    student_id="RS9101", course="AI and Robotics",
    staff_id="T5678", position="Research Assistant", 
    subject="Machine Learning", department="Computer Science", 
    research_topic="Deep Learning for Robotics"
)
research_student.display_research_student_info()
