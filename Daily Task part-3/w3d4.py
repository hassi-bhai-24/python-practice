"""
Encapsulation
● Public vs private attributes (_ and __)
● Property decorators
● Practice: Refactor classes with proper encapsulation
Encapsulation 
            It is about protecting data inside a class.It 
means keeping data (properties) and methods together in a class,
while controlling how the data can be accessed from outside the 
class.This prevents accidental changes to your data and hides 
the internal details of how your class works.
Why Use Encapsulation?
Encapsulation provides several benefits:
Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified
"""
class math:
    def __init__(self,num1,num2):
       self.num1 = num1
       self.num2 = num2

    @property
    def square(self):
        return self.num1*self.num2
s = math(2,2)
print(s.square)


class sum:
    def __init__(self,):
        self.a=int(input("Enter Num-a: "))
        self.b=int(input("Enter Num-b: "))
    @property
    def add(self):
        return self.a + self.b
        
s=sum()    
print(s.add)


