import java.sql.*;

public class DBManager {
	// JDBC driver name and database URL
	private final String jdbcDriver = "com.mysql.jdbc.Driver";  
	private String dbURL = "";//"jdbc:mysql://localhost/EMP";

	//  Database credentials
	private String user = "";
	private String pass = "";

	private Connection conn = null;
	private Statement stmt = null;

	DBManager (String _dbURL, String _user, String _pass) {
		dbURL = _dbURL;
		user = _user;
		pass = _pass

		connect();
	}

	public int connect (){
	   try{
	      //STEP 2: Register JDBC driver
	      Class.forName(jdbcDriver);

	      //STEP 3: Open a connection
	      System.out.println("Connecting to database...");
	      conn = DriverManager.getConnection(dbURL, user, pass);
	   }catch(SQLException se){
	      //Handle errors for JDBC
	      se.printStackTrace();
	   }catch(Exception e){
	      //Handle errors for Class.forName
	      e.printStackTrace();
	   }finally{
	      //finally block used to close resources
	      try{
	         if(stmt!=null)
	            stmt.close();
	      }catch(SQLException se2){
	      }// nothing we can do
	      try{
	         if(conn!=null)
	            conn.close();
	      }catch(SQLException se){
	         se.printStackTrace();
	      }//end finally try
	   }//end try
	}

	public int addInstance (String productName, double price, String local, char rateLocal) {

	}

	return 0;
}