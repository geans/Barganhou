import mysql.connector
from product_info import ProductInfo
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

class DBHandle ():
    def __init__ (self, user, password, host):
        self.config = (user, password, host)
        self.table_name = 'products'
        self.database_name = 'productlog'
    
    def __connect (self):
        self.connetion = mysql.connector.connect(*self.config)
        self.__select_database()
        self.cursor = self.connetion.cursor()


    def __disconnect (self):
        self.cursor.close()
        self.connetion.close()


    def __create_database (self):
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER "
                           "SET 'utf8'".format(self.database_name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
    
    
    def __create_table (self):
        table_scheme = ("CREATE TABLE `{}`("
                        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
                        "  `product_name` varchar(20) NOT NULL,"
                        "  `price` float NOT NULL,"
                        "  `amount` int(4) NOT NULL,"
                        "  `date_log` date NOT NULL,"
                        "  `local` varchar(20),"
                        "  `pucharse` enum('y', 'n'),"
                        "  PRIMARY KEY (`id`)"
                        ")".format(self.table_name))
        try:
            self.cursor.execute(table_scheme)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Failed to create table: already exists.")
            else:
                print(err.msg)
    
    
    def __select_database (self):
        try:
            self.connetion.database = self.database_name    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.__create_database()
                self.connetion.database = self.database_name
                self.__create_table();
            else:
                print(err)
    
    
    def bulk_insert (self, bulk_data):
        if not(type(bulk_data) is ProductInfo):
            return None
        self.__connect()
        add_scheme = ("INSERT INTO {} "
                      "(product_name, price, amount, date_log, local, pucharse"
                      "VALUES (%s, %s, %s, %s, %s, %s)".format(self.table_name))
        while not bulk_data.is_empty():
            self.cursor.execute(add_scheme, bulk_data.pop())
        self.connetion.commit()
        self.__disconnect()
        return 0


    def query_by_name (self, product_name):
        self.__connect()
        select_scheme = ("SELECT {} FROM {} WHERE "
            "product_name = %s".format('product_name', self.table_name))
        self.cursor.execute(select_scheme, product_name)
        self.__disconnect()
    
    
    def __str__(self):
        return "  Config: {}\n  Database name: {}\n  Table name: {}".format(
                self.config, self.database_name, self.table_name)



x = ProductInfo()
x.add('feijão', 3.5, 3, date(2015,8,8), 'Atacadão', 'yes')
h = x.pop()
print (h)
