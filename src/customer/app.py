from flask import Flask, render_template, url_for, request, flash, redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = 'hello'
	
def get_db():
	return mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='root',
		database='movie_ticketing_system'
		)

@app.route('/', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
		signupAccount()
		return redirect(url_for('signup'))

	return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		pass
	
	return render_template('login.html')

def signupAccount():
	db = get_db()
	cursor = db.cursor()

	try:
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email_address = request.form['email_address']
		mobile_number = request.form['mobile_number']
		age = request.form['age']

		cursor.execute('SELECT customer_id FROM customer WHERE email_address=%s OR mobile_number=%s', (email_address, mobile_number))
		row = cursor.fetchone()

		if not row:
			cursor.execute('INSERT INTO customer(first_name, last_name, email_address, mobile_number, age) VALUES(%s, %s, %s, %s, %s)', (first_name, last_name, email_address, mobile_number, age))
			db.commit()
			flash('Successfully registered account', 'info')
		else:
			flash('Email or number already exists', 'error')

	except mysql.connector.IntegrityError as e:
		pass
	finally:
		cursor.close()
		db.close()

if __name__ == '__main__':
	app.run(debug=True)