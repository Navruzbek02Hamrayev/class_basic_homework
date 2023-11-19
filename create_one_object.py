
class Person :
    def __init__(self,name: str) :
        self.name = name
    def info(self) -> str :
        return self.name
n = Person(
    name = "Ali"
)
#create an object named "person" whose name is "Ali"
print(n.info())