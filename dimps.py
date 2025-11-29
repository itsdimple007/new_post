# i love you my darling!
  

# class employee:
#     def __init__ (self,name,surname,gender,age):
#         self.name=name
#         self.surname=surname
#         self.gender=gender
#         self.age=age
        
        
    
#     def show(self):
#         print("ur name is: ",self.name)
#         print("surname kon btayega: ",self.surname)
#         print("gender plz: ",self.gender)
#         print("age bata jaldi: ",self.age)
        
        
# e = employee("Vinay","shuku","male",20)


# class bhumika(employee):
#     def show_details(self):
#         # print("ur name is: ",self.name)
#         # print("surname kon btayega: ",self.surname)
#         # print("gender plz: ",self.gender)
#         # print("age bata jaldi: ",self.age)
#         print("I am sexy as per my darling")

# b = bhumika("bhumika","jangid","female",19)
# b.show_details()

# class employee:
#     def __init__(self, name, surname, gender, age):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.age = age
    
#     def show(self):
#         print("ur name is: ", self.name)
#         print("surname kon btayega: ", self.surname)
#         print("gender plz: ", self.gender)
#         print("age bata jaldi: ", self.age)

# # Create an instance of employee
# e = employee("Vinay", "shuku", "male", 20)
# # e.show()  # This will work fine

# class bhumika(employee):
#     def show_details(self):
#         print("I am sexy as per my darling")

# # Create an instance of bhumika
# b = bhumika("bhumika", "jangid", "female", 19)
# b.show()  # This will work because `show_details` exists in `bhumika`
# b.show_details()

class Dimple:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Your name is: ",self.name)
        print("Enter your age:",self.age)

d=Dimple("Bhumika",20)
# d.show()           

class Vinay(Dimple):
    def __init__(self, name, age,gender):
        super().__init__(name,age)
        self.gender=gender

    def showw(self):
        print("Your name is: ",self.name)
        print("Enter your age:",self.age)
        print("Enter your gender: ",self.gender)

v=Vinay("Vinu",21,"Male")
# v.showw()               

class Love(Vinay):
    def __init__(self,name,age,gender,sname):
        super().__init__(name,age,gender)
        self.sname=sname

    def showww(self):
         print("Your name is: ",self.name)
         print("Enter your age:",self.age)
         print("Enter your gender: ",self.gender)
         print("Enter your gender here: ",self.sname)

l=Love("Vinay",21,"Male","Bhumika")     
l.showww()       