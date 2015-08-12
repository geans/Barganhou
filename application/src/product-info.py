class ProductInfo ():
    def __init__ (self):
        self.__queue = None
    
    
    def add (self, _product_name, _price, _amount, _date_log, _local, _pucharse):
        if (self.__queue is None):
            self.__queue = [_product_name, _price, _amount, _date_log, _local, _pucharse]
        else:
            self.__queue.append(_product_name, _price, _amount, _date_log, _local, _pucharse)
        
     
    def get (self):
        return (self.product_name, self.price, self.amount,
                self.date_log, self.local, self.pucharse)
    
    
    def size (self):
        if (self.__queue is None):
            return 0
        else:
            return len(self.__queue)

    
    def __str__ (self):
        return "{}, {}, {}, {}, {}, {}".format(*self.get())
