class ProductInfo ():
    def __init__ (self):
        self.__queue = []
    
    
    def add (self, _product_name, _price, _amount, _date_log, _local, _pucharse):
        self.__queue.append((_product_name, _price, _amount, _date_log, _local, _pucharse))
        
     
    def pop (self):
        if self.size() > 0:
            return self.__queue.pop(0)
        else:
            return None


    def size (self):
        return len(self.__queue)
        
    
    def is_empty (self):
        return self.size() is 0

    
    def __str__ (self):
        return "{}, {}, {}, {}, {}, {}".format(*self.get())





