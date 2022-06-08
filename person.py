

class Person:
    def __init__(self,_name,_age) :
        self.name = _name
        self.age = _age


    def sayHi(self):
        print('Hello my Name is' +str(self.name) + 'and i am'+  str(self.age)+ 'years old')
person1 = Person("Bob", 16)
person1.sayHi()
person2 = Person("James",22)
person2.sayHi()
person3 = Person("Sheryl",18)
person3.sayHi()