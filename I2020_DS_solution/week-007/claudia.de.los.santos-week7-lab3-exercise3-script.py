class Person:
    def __init__(self, name, birthday, age, location):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.location = location
    
    def change_name(self, name):
        self.name = name
    
    def change_age(self, age):
        self.age = age
    
    def change_location(self, location):
        self.location = location
    def say_hello(self):
        return f"Hello my name is {self.name}."

if __name__ == "__main__":
    import sys
    person_info = sys.argv
    person1 = Person(*person_info[1:])
    print(person1.say_hello())
    
