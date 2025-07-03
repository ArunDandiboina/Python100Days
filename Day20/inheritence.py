class Animal:
    def __init__(self):
        self.name = "Animal"
        self.infos = "This is an animal"
        
    def speak(self):
        print("Animal speaks")
    
    def info(self):
        print(f"This is a {self.name}")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.name = "Dog"
        
    def speak(self):
        print("Woof! Woof!")  

d = Dog()
d.speak()  # Output: Woof! Woof!
# speak parent class
d.info()    # Output: This is a Dog
print(d.infos)





