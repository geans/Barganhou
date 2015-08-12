import unittest
from db_handle import DBHandle
from product_info import ProductInfo

USER='guest'
PASS='123'
HOST='localhost'
config=(USER, PASS, HOST)

#class TestDBHandle(unittest.TestCase):
#def __init__ (self):
dbh = DBHandle(USER, PASS, HOST)
datalog = ('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes')
datalog2 = (('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes'),
            ('macarrão', 1.5, 8, (8,8,2015), 'Atacadão', 'yes'))


def test_insert ():
    assertEqual(dbh.bulk_insert(*datalog), 0)
    assertEqual(dbh.bulk_insert(*datalog2), 0)

    
def test_query ():
    dbh.bulk_insert(*datalog)
    dbh.bulk_insert(*datalog2)



#class TestProductInfo(unittest.TestCase):
def test_add_pop():
    x = ProductInfo()
    data = ('feijão', 3.5, 3, (2015,8,8), 'Atacadão', 'yes')
    x.add(*data)
    assertEqual(data, x.pop())



if __name__ == '__main__':
    unittest.main()
