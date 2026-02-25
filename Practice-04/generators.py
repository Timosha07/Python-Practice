#1
import math
n=int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= n:
      x = self.a
      self.a += 1
      return math.pow(x,2)
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter number: "))
print(", ".join(str(num) for num in even_numbers(n)))
#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input("Enter number: "))
print(", ".join(str(num) for num in divisible_by_3_and_4(n)))
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter start: "))
b = int(input("Enter end: "))

for value in squares(a, b):
    print(value)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter number: "))

for num in countdown(n):
    print(num)
   