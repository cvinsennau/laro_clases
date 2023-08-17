# Part I: Members, Students and Instructors
# You're starting your own web development school called Codebar! Everybody at Codebar - whether they are attending workshops or teaching them - is a Member:

# Each member has a full_name.
# Each member should be able to introduce themselves (e.g., "Hi, my name is Kevin!").
# Each Member is also either a Student or an Instructor:

# Each Student has a reason for attending Codebar (e.g., "I've always wanted to make websites!").
# Each Instructor a bio (e.g., "I've been coding in Python for 5 years and want to share the love!").
# Each Instructor also has a set of skills (e.g., ["Python", "Javascript", "C++"]).
# An Instructor can gain a new skill using add_skill.

class Member:
    def __init__(self, fullname):
        self.fullname = fullname 

    def hello(self):
        print(f"Hola! Soy {self.fullname}")
    

class Student(Member):
    def __init__(self,fullname,reason):
        super().__init__(fullname)
        self.reason = reason
    
class Instructor(Member):
    def __init__(self,fullname,bio,skills = []):
        super().__init__(fullname)
        self.bio = bio
        self.skills = skills
    
    def addSkill(self, skill):
        self.skills.append(skill)
        print(f"Tus skills son ${self.skills}")

cande = Student('Cande Vinsennau','Aprender')
cande.hello()

laro = Instructor('Laro','Laroman',['Promete','Programa'])
laro.hello()
laro.addSkill('Birra')


##

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def __repr__(self):
        return 'Person(' + self.name + ',' + str(self.age) + ')'
    
    def __add__(self,newPerson):
        newName = self.name + newPerson.name
        newAge = self.age + newPerson.age
        return Person(newName,newAge)
    
juan = Person('Juan',26)
laro = Person('Laro',38)

x = laro + juan

print(x)