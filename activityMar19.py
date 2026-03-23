"A class is a blueprint or template used to create objects, while an object is an actual instance of that class with real values."

"An object property is a variable that stores data about the object, while an object method is a function that performs an action using the object's data."


class Student:
        def __init__(self, name, age, grade, gpa, is_honor):
    self.name = name 
self.age = age 
self.grade = grade 
self.gpa = gpa 
self.is_honor = is_honor


    def add_bonus_points(self):
    self.gpa = self.gpa + 0.5
return self.gpa


def update_grade(self, new_grade):
    self.grade = new_grade
return self.grade


def check_honor_roll(self):
    if self.gpa >= 3.5:
    return "Honor Roll"
    else:
return "Not Honor Roll"
