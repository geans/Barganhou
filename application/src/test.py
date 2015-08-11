import unittest
import db-handle

USER='guest'
PASS='123'
HOST='localhost'

class TestDBHandle(unittest.TestCase):
    self.dbh = db-handle.DBHandle(USER, PASS, HOST)
    
    
    def test_insert (self):
        datalog = {'leite pó', 3.0, 10, date(8,8,2015), 'Atacadão', 'yes'}
        datalog2 = {{'leite pó', 3.0, 10, date(8,8,2015), 'Atacadão', 'yes'},
                    {'macarrão', 1.5, 8, date(8,8,2015), 'Atacadão', 'yes'}}
        self.assertEqual(self.dbh.bulk_insert(*datalog), 1)
        self.assertEqual(self.dbh.bulk_insert(*datalog2), 2)

        
    def test_query (self):
        datalog = {'leite pó', 3.0, 10, date(8,8,2015), 'Atacadão', 'yes'}
        datalog2 = {{'leite pó', 3.0, 10, date(8,8,2015), 'Atacadão', 'yes'},
                    {'macarrão', 1.5, 8, date(8,8,2015), 'Atacadão', 'yes'}}
        self.dbh.bulk_insert(*datalog)
        self.dbh.bulk_insert(*datalog2)



if __name__ == '__main__':
    unittest.main()
