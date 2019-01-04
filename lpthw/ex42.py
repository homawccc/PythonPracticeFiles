## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is an object (sort of)
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person may not (initially) have a pet
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Its calling super function to inherit Person Class name & age
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog named "Rover"
rover = Dog("Rover")

## satan is-a cat named "Satan"
satan = Cat("Satan")

## mary is a Person named "Mary"
mary = Person("Mary")

## mary has-a pet who is-a cat nmaed Satan
mary.pet = satan

## frank is-a employee named "Frank who has-a 120000 salary"
frank = Employee("Frank", 120000)

## frank has-a pet named rover (who is-a dog)
frank.pet = rover

## flipper is-a intance of the Fish() class
flipper = Fish()

## crouse is-a intance of the Salmon() class
crouse = Salmon()

## harry is-a instance of the Halibut() class
harry = Halibut()