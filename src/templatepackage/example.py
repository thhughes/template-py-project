
class Example: 
    E_DEFAULT='Hello World'
    def __init__(self, *args, **kwargs): 
        self.__e = kwargs.get('E', self.E_DEFAULT)
    
    def get(self): 
        return self.__e
    