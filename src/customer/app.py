from flask import Flask, render_template, url_for, request
import mysql.connector

app = Flask(__name__)
	
def get_db():
	return mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root",
		database="movie_ticketing_system"
		)

@app.route('/', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
		db = get_db();
		cursor = db.cursor()

		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email_address = request.form['email_address']
		mobile_number = request.form['mobile_number']
		age = request.form['age']

		cursor.execute("INSERT INTO customer(first_name, last_name, email_address, mobile_number, age) VALUES(%s, %s, %s, %s, %s)", (first_name, last_name, email_address, mobile_number, age))
		db.commit()
		cursor.close()
		db.close()

		return render_template('signup.html')
	
	return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		pass
	
	return render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True)