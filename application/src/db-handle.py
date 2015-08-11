import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

class DataCollection ():
    def add (product_name, price, amount, date_log, local, pucharse):
        self.product_name = product_name
        self.price = price
        self.amount = amount
        self.date_log = date_log
        self.local = local
        self.pucharse = pucharse


class DBHandle ():
    def __init__ (self, user, password, host):
        self.config = {user, password, host}
        self.table_name = 'products'
        self.database_name = 'productlog'
    
    def __connect (self):
        self.connetion = mysql.connector.connect(**self.config)
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
    
    
    def bulk_insert (self, bulk_data, number_instances):
        self.__connect()
        add_scheme = ("INSERT INTO {} "
                      "(product_name, price, amount, date_log, local, pucharse"
                      "VALUES (%s, %s, %s, %s, %s, %s)".format(self.table_name))
        compare = tuple is type(product_name) is type(price) is type(amount)
        compare = (tuple is type(date_log)is type(local) is type(pucharse)) is compare
        compare = compare is True
        number_tuples = 1
        if compare:
            number_tuples = min(len(product_name), len(price), len(amount),
                                len(date_log), len(local), len(pucharse))
            i = 0
            while i < number_tuples:
                datalog = (product_name[i], price[i], amount[i])
                datalog += (date_log[i], local[i], pucharse[i])
                self.cursor.execute(add_scheme, datalog)
                i += 1
            self.connetion.commit()
        else:
            datalog = (product_name, price, amount, date_log, local, pucharse)
            self.cursor.execute(add_scheme, datalog)
        self.connetion.commit()
        self.__disconnect()
        return number_tuples


    def query_by_name (self, product_name):
        self.__connect()
        select_scheme = ("SELECT {} FROM {} WHERE "
            "product_name = %s".format(product_name, self.table_name))
        self.cursor.execute(select_scheme, product_name)
        self.__disconnect()
    
    
    def __str__(self):
        return 


