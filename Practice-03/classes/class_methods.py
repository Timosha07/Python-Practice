class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Dias")
p1.greet()



class Class:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def summ(self):
    print(self.a + self.b)  
p1 = Class(15,16) 
p1.summ()



class Class:
  def plus(self,a,b):
    return a + b
  def multiply(self,a,b):
    return a * b
aa = int(input())
bb = int(input())
p1 = Class()
print(p1.plus(aa,bb))
print(p1.multiply(aa,bb))  



class Class:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return (f"{self.name} is my name and my age is {self.age}")  
p1 = Class("Tobias",145)    
print(p1) 