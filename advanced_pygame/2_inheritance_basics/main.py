class Cat():
    """A class to represent a general cat """

    def __init__(self, my_name, my_gender, my_age):
        """initialize atributes"""
        self.name = my_name
        self.gender = my_gender
        self.age = my_age
    
    def eat(self):
        """method: feed the dog"""
        if self.gender == "male":
            print("Here " + self.name + "! Good Boy! Eat up.")
        else:
            print("Here " + self.name + "! Good Girl! Eat up.")

    def meow(self, is_loud):
        """method: get the dog to speak"""
        if is_loud:
            print("MEEEOOOOOWWWWW ! MEEEEOOOOOOWWWW !")
        else:
            print("meowww...")

    def compute_age(self):
        """method: compute the age in cat years"""
        cat_age = self.age*7
        print(self.name + "is " + str(cat_age) + " years old in cat years")

#class Tiger which inherit from Cat class
class Tiger(Cat):
    """class to represent a specific type of cat"""
    def __init__(self, my_name, my_gender, my_age, is_hunting):
        #call the initialization of the super (parent) class
        super().__init__(my_name, my_gender, my_age)
        self.is_hunting = is_hunting

    def hunt(self):
        """if the cat is_hunting, take them for a hunting"""
        if not self.is_hunting:
            self.meow(False)
            print(self.name + " is a shy tiger who doesn't like to hunt.")
        else:
            print(self.name + " will hunt excellent!")

    #update (overwrite) meow to have it specific for tigers.
    def meow(self, is_loud):
        """Get the cta meow/ roar"""
        if is_loud:
            print("ROAAARRRR! ROOOOAAAAAARRRRR! RRROOOOAARRR!")
        else:
            print("rrruuuurr...")



tiger = Tiger("Kitty", "female", 10, True)
tiger.eat()
tiger.meow(True)
tiger.compute_age()
print()
tiger.hunt()

#The Cat class can't hunt
cat = Cat("Grey cat", "male", 5)
#cat.hunt() - it will not work

cat.meow(True)
