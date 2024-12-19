# Write a program to build a home. The Home class should define all the attributes of each room in a home.
# FirstHome  and SecondHome. First home should have an extra study room as a method.
# SecondHome should have the work_area as an extra method. Should use the concept of inheritance.

class Home:
    def __init__(self, living_room, dining_room, num_bedrooms, num_bathrooms, kitchen):
        self.living_room = living_room
        self.dining_room = dining_room
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.kitchen = kitchen

    def describe(self):
        print(f"This Home has a living room of {self.living_room} square feet, \n dining room of {self.dining_room} square feet,\n {self.num_bedrooms} bedrooms, \n {self.num_bathrooms} bathrooms, \n and a Kitchen of {self.kitchen} square feet")

    def Add_study_room(self):
        self.study_room_size = 200

    def Add_work_area(self):
        self.work_area_size = 100

class FirstHome(Home):
    def __init__(self, living_room, dining_room, num_bedrooms, num_bathrooms, kitchen):
        super().__init__(living_room, dining_room, num_bedrooms, num_bathrooms, kitchen)

    def Add_study_room(self):
        super().Add_study_room()
        print(f"The FirstHome now has a {self.study_room_size} square feet study room")

class SecondHome(Home):
    def __init__(self, living_room, dining_room, num_bedrooms, num_bathrooms, kitchen):
        super().__init__(living_room, dining_room, num_bathrooms, num_bedrooms, kitchen)

    def Add_work_area(self):
        super().Add_work_area()
        print(f"The SecondHome now has a {self.work_area_size} square feet work area")

first_home = FirstHome(400, 400, 4, 5, 300)
first_home.describe()
first_home.Add_study_room()

print("====================================================================================================")

second_home = SecondHome(300, 300, 3, 4, 200)
second_home.describe()
second_home.Add_work_area()

