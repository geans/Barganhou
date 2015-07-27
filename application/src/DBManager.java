import java.sql.*;

public class DBManager {
	private static final String PRODUCT_NAME_COLUMN = "ProductName";
	private static final String TABLE = "CatalogOfPrice";
	
	// JDBC driver name and database URL
	private final String jdbcDriver = "com.mysql.jdbc.Driver";  
	private String dbURL; // "jdbc:mysql://localhost/EMP";
	
	//  Database credentials
	private String user = "";
	private String pass = "";
	
	private Connection conn = null;
	private Statement stmt = null;
	
	DBManager (String _dbURL, String _user, String _pass) {
		dbURL = _dbURL;
		user = _user;
		pass = _pass;
	
		connect();
	}
	
	private void debug (String text) {
		System.out.println (text);
	}
	
	public int connect (){
	   try{
	      //STEP 2: Register JDBC driver
	      Class.forName(jdbcDriver);
	
	      //STEP 3: Open a connection
	      debug("Connecting to database...");
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
	    	  // TODO
	    	  debug(se2.toString());
	      }// nothing we can do
	      try{
	         if(conn!=null)
	            conn.close();
	      }catch(SQLException se){
	    	  debug(se.toString());
	      }//end finally try
	   }//end try
	   
	   return 0;
	}
	
	public boolean addInstance (String productName, float price, 
			String local, char rateLocal) {
		String sql = "INSERT INTO "+TABLE+" VALUES ("+productName
				+", "+price+", "+local+", "+rateLocal+")";
		boolean ret = false;
		try {
			ret = stmt.execute(sql);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			debug(e.toString());
		}
		return ret;
	}
	
	public String getInstanceForName (String productName) {
		String sql = "SELECT * FROM "+TABLE+" WHERE "+PRODUCT_NAME_COLUMN+" = "+productName;
		ResultSet resultQuery = null;
		try {
			resultQuery = stmt.executeQuery(sql);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			debug(e.toString());
		}
		return resultQuery.toString();
	}
}