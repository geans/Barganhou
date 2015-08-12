import unittest
from db_handle import DBHandle
from product_info import ProductInfo

USER='guest'
PASS='123'
HOST='localhost'
dbh = DBHandle(USER, PASS, HOST)
datalog = ('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes')
datalog2 = (('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes'),
            ('macarrão', 1.5, 8, (8,8,2015), 'Atacadão', 'yes'))

def test_DBHandle_insert_query ():
    assertEqual(dbh.bulk_insert(*datalog), 0)
    assertEqual(dbh.bulk_insert(*datalog2), 0)


def test_ProductInfo_add_pop_size():
    x = ProductInfo()
    x.add(*datalog)
    assertEqual(datalog, x.pop())
    assertEqual(x.size(), 0)
    x.add(*datalog2[0])
    assertEqual(x.size(), 1)
    x.add(*datalog2[1])
    assertEqual(x.size(), 2)
    assertEqual(datalog2[0], x.pop())
    assertEqual(x.size(), 1)
    assertEqual(datalog2[1], x.pop())
    assertEqual(x.size(), 0)
    assertEqual(None, x.pop())
    assertEqual(x.size(), 0)


if __name__ == '__main__':
    unittest.main()
