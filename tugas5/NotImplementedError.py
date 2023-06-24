class MyClass:
    def my_method(self):
        raise NotImplementedError("Subclasses must override this method")
        
my_object = MyClass()
my_object.my_method()