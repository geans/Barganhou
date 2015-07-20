#include <string>
#include <mysql/mysql.h>




use std::string;

class db-interface {

	db-interface(string _host, string _user, string _passwd, string _dbname) {
		host = _host;
		user = _user;
		passwd = _passwd;
		dbname = _dbname;
		conn = mysql_init(NULL);
	}

	int connect (){
		return mysql_real_connect (conn, HOST, USER, PASS, DB, 0, NULL, 0);
	}

	int insert_instance(string product_name, double price, string local, 
		float confidence_level_local);

	int altere_instance(string product_name, double price, string local, 
		float confidence_level_local);

	int remove_instance(int id_instance);

	string get_all_instance();

	string find_inst_for_name(string product_name);

	string find_inst_for_local(string product_name);

private:
	string host;
	string user;
	string passwd;
	string dbname;
	MYSQL *conn;
}