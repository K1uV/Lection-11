class Person():
    def __init__(self, name, surname, age, form):
        self.name = name
        self.surname = surname
        self.age = age
        self.form = form

    def justlive(self):
        print(self.name + ' ' + 'just live')
    
    def haveproblems(self):
        print(self.name + ' ' +  self.surname.title() + ' ' + 'have some problems')

my_person = Person('Dima', 'Kylibaba', '20', '14-B')
my_person.justlive()
my_person.haveproblems()

class Student():
    def __init__(self, name, surname, age, form):
        self.name = name
        self.surname = surname
        self.age = age
        self.form = form

    def losebooks(self):
        print(self.name + ' ' + 'lose his books((')
    
    def sleeptoolong(self):
        print(self.name + ' ' + self.surname.title() + ' ' + 'slept his lessons.')


my_student = Student('Vanya', 'Petrov', '21', '2 course')
my_student.losebooks()
my_student.sleeptoolong()


class Teacher():
    def __init__(self, name, surname, age, salary, form, lesson):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.form = form
        self.lesson = lesson

    def marktwo(self):
        print(self.name.title() + ' ' + 'give u a mark F')
    
    def markeleven(self):
        print(self.name.title() + ' ' + 'give u a mark A')
    
    def salarynima(self):
        print(self.name + ' ' + 'dont earn' + ' ' + self.salary + ' ' + 'salary')
    

my_teacher = Teacher('Julia', 'Math-teacher', '44', '14000', '10-C', 'Math')
my_teacher.marktwo()
my_teacher.markeleven()
my_teacher.salarynima()
