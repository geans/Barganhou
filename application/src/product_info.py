class ProductInfo ():
    def __init__ (self):
        self.__queue = []
    
    
    def add (self, product_name, price, amount, date_log, local, pucharse):
        self.__queue.append((product_name, price, amount, date_log, local, pucharse))
        
     
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
        return "{}".format(self.queue)


