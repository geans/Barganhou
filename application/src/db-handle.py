import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

class DBHandle ():
    def __init__ (self, user, password, host):
        self.user = user
        self.password = password
        self.host = host
    
    def __connect_sql (self):
        self.connetion = mysql.connector.connect(self.user, self.database)
        self.cursor = self.connetion.cursor()


    def __disconnect_sql (self):
        self.cursor.close()
        self.connetion.close()


    def __create_database (self, database_name):
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
    
    
    def __create_table (self):
        table_scheme = ("CREATE TABLE `product`("
                        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
                        "  `product_name` varchar(20) NOT NULL,"
                        "  `price` float NOT NULL,"
                        "  `amount` int(4) NOT NULL,"
                        "  `date_buy` date NOT NULL,"
                        "  `local` varchar(20),"
                        "  PRIMARY KEY (`id`)"
                        ")")
        try:
            self.cursor.execute(table_scheme)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Failed to create table: already exists.")
            else:
                print(err.msg)
    
    
    def __connect_database (self, database_name = 'productlog'):
        try:
            self.connetion.database = database_name    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.__create_database(database_name)
                self.__create_table();
                self.connetion.database = database_name
            else:
                print(err)
    
    
    def insert_instance (self, product_name, price, amount, date_buy, local=''):
        add_scheme = ("INSERT INTO productlog "
                      "(product_name, price, amount, date_buy, local"
                      "VALUES (%s, %s, %s, %s, %s)")
        datalog = (product_name, price, amount, date_buy, local)
        self.cursor.execute(add_scheme, datalog)
        self.connetion.commit()
