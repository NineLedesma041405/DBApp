## How to run

1. Check if flask and mysql connector is intalled
2. Run the sql file in the workbench to create the database with the customer table
3. In app.py, modify this part of the code if needed:

```
def get_db():
	return mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root",
		database="movie_ticketing_system"
		)
```

Change the host, user, and password if needed

3. Open customer folder in the terminal
4. Enter python3 app.py to run the program
5. Copy paste the IP address
6. Paste the address in a web browser 