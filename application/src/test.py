import unittest
from db_handle import DBHandle
from product_info import ProductInfo

USER='guest'
PASS='123'
HOST='localhost'
dbh = DBHandle(USER, PASS, HOST)
datalog1 = ('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes')
datalog2 = (('leite pó', 3.0, 10, (8,8,2015), 'Atacadão', 'yes'),
            ('macarrão', 1.5, 8, (8,8,2015), 'Atacadão', 'yes'))

class TestCases (unittest.TestCase):

    def test_DBHandle (self):
        pi1 = ProductInfo()
        pi2 = ProductInfo()
        pi1.add(*datalog1)
        pi2.add(*datalog2[0])
        pi2.add(*datalog2[1])
        self.assertEqual(dbh.bulk_insert(pi1), 0)
        self.assertEqual(dbh.bulk_insert(pi2), 0)

    def test_ProductInfo (self):
        pi1 = ProductInfo()
        pi2 = ProductInfo()
        self.assertEqual(pi1.size(), 0)
        self.assertEqual(pi2.size(), 0)
        pi1.add(*datalog1)
        pi2.add(*datalog2[0])
        pi2.add(*datalog2[1])
        self.assertEqual(pi1.size(), 1)
        self.assertEqual(pi2.size(), 2)
        self.assertEqual(pi1.pop(), datalog1)
        self.assertEqual(pi1.size(), 0)
        self.assertEqual(pi2.pop(), datalog2[0])
        self.assertEqual(pi2.size(), 1)
        self.assertEqual(pi2.pop(), datalog2[1])
        self.assertEqual(pi2.size(), 0)
        self.assertEqual(pi2.pop(), None)
        self.assertEqual(pi2.size(), 0)



if __name__ == '__main__':
    unittest.main()
