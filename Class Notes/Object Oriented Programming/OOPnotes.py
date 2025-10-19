#classes are inventing your own data types
#class is definition object is the instance of a class
#mutable but can be made imutable
#methods = functions in classes you can define that work in a special way allow you to determine behavior in a special way
#__INIT__ initialize the contents of an object. This is the function. self is used to store the values. self give you access to the object 
#that was jsut created
#str and init are function if you define str and something wants to see your object as a string like print this will return that "a student"
#property attribute with more control and defenses in place
#decorators functions that modify the behavorior of other functions
# When should you use a class. When you want to represent a real world entitiy or somehting that reuqires attributes

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
           
        self.name = name 
        self.house = house 


    def __str__(self):
        return f"{self.name} is from {self.house}."
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            ValueError("Missing Name")
        self._name = name
    
    #Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Reavenclaw"]:
            raise ValueError("Invalid House")
        self._house = house
    

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

main()