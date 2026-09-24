# Build a small program, that represents a bootcamp
# a Bootcamp should have a name and should store Person objects
# and:
# - it should be able to add new Persons(students) to the bootcamp
# - it should show us the list of Person objects
# - it should tell us the total number of Person objects on bootcamp

from exercise_medium import Person

# Bootcamp
# parameters
# - name, string eg. Makers
# attributes
# - name
# - students, list eg. [student1, student2]
class Bootcamp:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def __repr__(self):
        return f"Bootcamp(name={self.name}, students={self.students})"

# add_student(person)
# Parameters: person, Person
# Returns: None
# Side effect: push the student into the self.students list
    def add_student(self, person):
        self.students.append(person)

# get_students()
# Parameters: None
# Returns: list, eg. [student1, student2]
# Side effects: None
    def get_students(self):
        return self.students
        
# get_number_of_students()
# Parameters: None
# Returns: int, eg. 5
# Side effects: None
    def get_number_of_students(self):
        return len(self.students)

bootcamp = Bootcamp("Makers")
print(bootcamp.name)
print(bootcamp.students)

person = Person("Hunor", 38, "waiter")
chibs = Person("Chibs", 20, "software engineer")

bootcamp.add_student(person)
bootcamp.add_student(chibs)

print("Printing students list of Bootcamp:")
print(bootcamp.students)
print("Checking if students/persons name is Hunor and Chibs:")
print(bootcamp.students[0].name)
print(bootcamp.students[1].name)

print("Printing list of students with get_students():")
print(bootcamp.get_students())

print("Printing number of students, which should be 2:")
print(bootcamp.get_number_of_students())

print(bootcamp)