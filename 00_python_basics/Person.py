class Person:
   def __init__(self, name,age,):
      self.name= name
      self.age= self.validate_age(age)
      pass
   
   def validate_age(self, age):
       if age > 0 and age < 100:
          self.age = age
       else:
           self.age = "error"
       return self.age 
   
   def get_age(self):
      return self.age 
   

p1=Person(name="Jason",age=1000)
print(p1.get_age())
       