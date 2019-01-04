# parent class
class Bird:
    
    def __init__(self):
        print("The Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()  # will also print "The Bird is ready"
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()   # instantiates Penguin class
peggy.whoisThis()   # calls function of the Penguin class
peggy.swim()        # calls swim function of the Bird class
peggy.run()         # calls run function of the Penguin class
bob = Bird()        # instantiates Bird class