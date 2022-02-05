#Rooms
class Classroom:
    type = "Classroom"
    
    def __init__(self, size, capacity, room_number, usable):
        if (usable == "True" or usable == "False"):
            self.usable = usable
        else:
            print ("usable has to have value of True or False!")
        self.size = size
        self.capacity = capacity
        self.room_number = room_number

    def __str__(self):
        if self.usable:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity} and it is usable" 
        else:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity} and it is not usable" 
        
class ExerciseHall(Classroom):
    type = "Exercise Hall"
    
    def __init__(self, size, capacity, room_number, usable, exercise_tools_amount):
        super().__init__(size, capacity, room_number, usable)
        self.exercise_tools_amount = exercise_tools_amount

    def __str__(self):
        if self.usable:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it contains {self.exercise_tools_amount} exercise tools and it is usable" 
        else:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it contains {self.exercise_tools_amount} exercise tools and it is not usable" 

class Laboratory(Classroom):
    type = "Laboratory"
    
    def __init__(self, size, capacity, room_number, usable, advanced_lessons):
        super().__init__(size, capacity, room_number, usable)
        if (advanced_lessons == "True" or advanced_lessons == "False"):
            self.advanced_lessons = advanced_lessons
        else:
            print ("advanced_lessons has to have value of True or False!")
        
    def __str__(self):
        if self.usable and self.advanced_lessons:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it is meant for advanced classes and it is usable" 
        elif self.usable and self.advanced_lessons == False:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it is meant for basic classes and it is usable"
        elif self.usable == False and self.advanced_lessons:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it is meant for advanced classes and it is not usable"
        else:
            return f"{self.type} {self.room_number} has a size of {self.size}, capacity is {self.capacity}, it is meant for basic classes and it is not usable"

#Staff
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} has the age of {self.age}" 

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
        self.lessons_taught = 0

    def teach_lesson(self):
        print (f"{self.name} taught a lesson about {self.subject}")
        self.lessons_taught = self.lessons_taught + 1

    def __str__(self):
        return f"{self.name} has the age of {self.age}. Teaches {self.subject}, gets paid {self.salary} and has taught {self.lessons_taught} lessons" 

class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades
        self.lessons_attended = 0

    def attend_lesson(self):
        print (f"{self.name} attended a lesson")
        self.lessons_attended = self.lessons_attended + 1

    def set_lessons_attended(self):
        self.lessons_attended = input("Set lessons attended by student {self.name} to: ")
       
    def __str__(self):
        return f"{self.name} has the age of {self.age}. Has average of grades {self.grades} and has attended {self.lessons_attended} lessons"

def move_screen():
    print("\n" * 2)

def print_instructions():
    print("*****************************************")
    print("0. Show instructions again")
    print("1. Add a classroom")
    print("2. Retrieve data about a classroom")
    print("3. Add a laboratory")
    print("4. Retrieve data about a laboratory")
    print("5. Add an exercise hall")
    print("6. Retrieve data about an exercise hall")
    print("7. Add a teacher")
    print("8. Retrieve data about a teacher")
    print("9. Have a teacher teach a lesson")
    print("10. Add a student")
    print("11. Retrieve data about a student")
    print("12. Have a student attend a lesson")
    print("*****************************************")
    move_screen()

list_of_teachers = []
list_of_students = []
list_of_classrooms = []
list_of_laboratories = []
list_of_exercise_halls = []

#Control
print("Hello! This is elementary school creator 1.0, what would you like to do?")
print_instructions()

while True:
    choice = input("Enter action from the list above (0...12). Press 0 for the list of instructions: ")
    if choice in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        if choice == '0':
            print_instructions()
        elif choice == '1':
            print("Please provide details for the classroom")
            list_of_classrooms.append(Classroom(input("Size: "), input("Capacity: "), input("Room number: "), input("Usable (True or False): ")))
        elif choice == '2':
            for obj in list_of_classrooms:
                print(obj)
        elif choice == '3':
            print("Please provide details for the laboratory")
            list_of_laboratories.append(Laboratory(input("Size: "), input("Capacity: "), input("Room number: "), input("Usable (True or False): "), input("Meant for advanced lessons (True or False): ")))
        elif choice == '4':
            for obj in list_of_laboratories:
                print(obj)
        elif choice == '5':
            print("Please provide details for the exercise hall")
            list_of_exercise_halls.append(ExerciseHall(input("Size: "), input("Capacity: "), input("Room number: "), input("Usable (True or False): "), input("Exercise tools amount: ")))
        elif choice == '6':
            for obj in list_of_exercise_halls:
                print(obj)                       
        elif choice == '7':
            print("Please provide details for the teacher")
            list_of_teachers.append(Teacher(input("Name: "), input("Age: "), input("Subject taught: "), input("Salary: ")))
        elif choice == '8':
            for obj in list_of_teachers:
                print(obj)
        elif choice == '9':
            choosen_item = next(person for person in list_of_teachers if person.name == input("Choose the persons name: " ))
            choosen_item.teach_lesson()
        elif choice == '10':
            print("Please provide details for the student")
            list_of_students.append(Student(input("Name: "), input("Age: "), input("Grades average: ")))
        elif choice == '11':
            for obj in list_of_students:
                print(obj)
        elif choice == '12':
            choosen_item = next(person for person in list_of_students if person.name == input("Choose the persons name: " ))
            choosen_item.attend_lesson()
    move_screen()
