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

#create two cat obects from cat class
cat_1 = Cat("Mechaś", "female", 9)
cat_2 = Cat("Nynek", "male", 3)
#print - to make separate clear line between next stuff :)
print() 


#access attriutes of each individual object
print(cat_1.name)
print(cat_2.gender)
#print - to make separate clear line between next stuff :)
print()

#updating attribute (overwritten):
cat_1.name = "Ścierusek"
print(cat_1.name)
#print - to make separate clear line between next stuff :)
print()

#call methods on the class
cat_1.eat()
cat_2.eat()
#print - to make separate clear line between next stuff :)
print()

cat_1.meow(True)
cat_2.meow(False)
#print - to make separate clear line between next stuff :)
print()

cat_1.compute_age()
cat_2.compute_age()
#print - to make separate clear line between next stuff :)
print()