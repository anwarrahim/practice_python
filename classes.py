class person():
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work= work
    def introduction(self):
        print("my name is " + self.name + " and i am " + str(self.age) + " years old and i am a " + self.work)

    def accupation(self):
        print("my name is " + self.name + " and i am a " + self.work)

#make the objects

person1 = person("Anwar Rahim", 20 , "engineer")
person2 = person("Ahmed", 20 , "doctor")
person3 = person("farhan", 20 , "programmer")





        