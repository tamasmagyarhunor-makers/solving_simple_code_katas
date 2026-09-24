# Build a small program that represents a Person
# a Person should have name, age, job title
# and:
# - it should be able to say hi,
# - it should be able to tell its age
# - it should be able to tell its job title

# Person
# parameters
# - name, string eg. "Hunor"
# - age, int eg. 38
# - job_title, string eg. "Coach"
class Person:
    def __init__(self, name, age, job_title):
        self.name = name
        self.age = age
        self.job_title = job_title
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job_title={self.job_title})"

# say_hi(who)
# Parameters: who, string, eg. Sophie
# Return: string, eg. say_hi("Sophie") => 
# => "Hi Sophie, my name is Hunor"
# Side effects: None
    def say_hi(self, who):
        return "Hi " + who + ", my name is " + self.name

# get_age()
# Parameters: None
# Return: int, eg. 38
# Side effects: None
    def get_age(self):
        return self.age

# get_job_title()
# Parameters: None
# Return: string, eg. "Coach"
# Side effects: None
    def get_job_title(self):
        return self.job_title

# hunor = Person("Hunor", 38, "Coach")

# # print(hunor.say_hi("Sophhie"))
# # print(hunor.get_age())
# print(hunor.get_job_title())