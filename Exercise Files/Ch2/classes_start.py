#
# Example file for working with classes
#

# class myClass():
#   def method1(self):
#     print("myClass method1")
  
#   def method2(self, someString):
#     print("myClass method2: " + someString)

# class anotherClass(myClass):
#   def method1(self):
#     # myClass.method1(self)
#     print("anotherClass method1")
  
#   def method2(self, someString):
#     print("anotherClass method2")

# def main():
#   c = myClass()

#   c.method1()
#   c.method2("I am the someString's value")

#   c2 = anotherClass()
#   c2.method1()
#   c2.method2("This is string")
 
 
def inc(a, b=1):
    return(a + b)
a=inc(1)
a=inc(a,a)
print(a)
  
# if __name__ == "__main__":

#   inc()
