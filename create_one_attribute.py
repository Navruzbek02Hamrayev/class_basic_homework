#Create a "Person" class
class Person :
#Create an attribute "name" in the "Person" class
    def __init__(self,name: str) :
        self.name = name
    def info(self) -> str :
        return self.name
n = Person(
    name = "Navruzbek"
)
print(n.info())
