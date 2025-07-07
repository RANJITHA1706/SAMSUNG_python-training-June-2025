# Create a singleton class
class Singleton:
    instance_variable = None

    def __new__(cls):
        if cls.instance_variable == None:
            cls.instance_variable = super(Singleton,cls).__new__(cls)
        return cls.instance_variable
    
a = Singleton()
b = Singleton()
print(a == b)
