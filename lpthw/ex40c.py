class Person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
		#would usually use...
		#self.firstname = firstname;
		#variable & parameter should match
		#but don't have to.

    def say_hi(self):
        print('Hello, my name is {} {}'.format(self.fname, self.lname))

p = Person('Rich', 'Homa')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()