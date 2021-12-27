class cat:
    def __init__(self,name,breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def speak(self):
        print(self.name+ "speaker")

mycat = cat("akki","house cat","skin color")        

print(mycat.name)
print(mycat.color) 
mycat.speak()     

mycat2 = cat("snowbell","classic russian","white")

print(mycat2.name)
print(mycat2.color)
print(mycat2.speak())

