"""
One would use @classmethod when he/she would want to change the behaviour of the method based on which subclass is calling the method. remember we have a reference to the calling class in a class method.

While using static you would want the behaviour to remain unchanged across subclasses

@classmethod means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we normally do with methods). 
This means you can use the class and its properties inside that method rather than a particular instance.

@staticmethod means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). 
This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).


"""


class Hero:

    @staticmethod
    def say_hello():
        print("Helllo...")

    @classmethod
    def say_class_hello(cls):
        if(cls.__name__ == "HeroSon"):
            print("Hi Kido")
        elif(cls.__name__ == "HeroDaughter"):
            print("Hi Princess")


class HeroSon(Hero):

    def say_son_hello(self):
        print("test  hello")


class HeroDaughter(Hero):

    def say_daughter_hello(self):
        print("test  hello daughter")


testson = HeroSon()

testson.say_class_hello()

testson.say_hello()

testdaughter = HeroDaughter()

testdaughter.say_class_hello()

testdaughter.say_hello()
