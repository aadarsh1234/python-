# Add a static method in problem 2.to greet the user with hello
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square is : {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"The squareroot  is : {self.n**0.5}")

    @staticmethod
    def hello():
        print("hello greet ")

num=float(input("Enter a number :"))
a=calculator(num)
a.square()
a.cube()
a.squareroot()
a.hello()

            
        