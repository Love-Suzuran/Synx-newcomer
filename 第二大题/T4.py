class animal:
    def speak(self):
        pass
class dog:
    def speak(self):
        print("汪汪")
class cat:
    def speak(self):
        print("喵喵")
def animal_speak(animal):
    return animal.speak();
dg=dog();
ct=cat();
animal_speak(dg)
animal_speak(ct)
