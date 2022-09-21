sqlcommands = (

    """
                CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL PRIMARY KEY,
                    firstname VARCHAR (30),
                    lastname VARCHAR (30),
                    username VARCHAR (30),
                    password VARCHAR (20),
                    email VARCHAR (30),
                    isadmin BOOLEAN DEFAULT FALSE NOT NULL,
                    registered TIMESTAMP DEFAULT NOW()
                    )
                """,
   
  
    """
                INSERT INTO users(firstname,lastname,username, password,email)      
                VALUES('Rhytah','Namono','admin','sup3rpsW','girl@world.com')                
                """
)
