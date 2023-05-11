'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:

    def __init__(self, age, name) : 
        self.name = name
        self.age = age 
    
    def increase_age(self) : 
        self.age = self.age + 1 
        print(self.age)

    def say_greeting(self) : 
        print("Hello world! My name is " + self.name + "!")

    def count_to_age(self) :
        count = 0 
        while count < self.age : 
            print(count)
            count = count + 1 
        


# You won't need to call anything here.