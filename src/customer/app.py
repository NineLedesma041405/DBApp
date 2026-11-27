from flask import Flask, render_template, url_for, request, flash, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'hello'

# ADMIN CREDENTIALS

ADMIN_EMAIL_ADDRESS = 'admin@gmail.com'
ADMIN_MOBILE_NUMBER = '09999999999'

def get_db():
	'''Connects the database to the app.'''

	return mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='root',
		database='movie_ticketing_system'
		)

@app.route('/', methods=['POST', 'GET'])
def signup():
	'''Displays the signup page and processes the signup form.'''

	if request.method == 'POST':
		signupAccount()
		return redirect(url_for('signup'))

	return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	'''Displays the login page and processes the login form.'''

	# If the admin logs in, redirect them to the customer module

	if request.method == 'POST':
		email_address = request.form['email_address']
		mobile_number = request.form['mobile_number']

		if email_address == ADMIN_EMAIL_ADDRESS and mobile_number == ADMIN_MOBILE_NUMBER:
			session['email_address'] = email_address
			session['mobile_number'] = mobile_number
			return redirect(url_for('customerModule'))

		loginAccount()
		return redirect(url_for('login'))
	
	session.pop('email_address', None)
	session.pop('mobile_number', None)
	return render_template('login.html')

@app.route('/customerModule', methods=['POST', 'GET'])
def customerModule():
	'''Displays the customer module.'''

	db = get_db()
	cursor = db.cursor()

	if 'email_address' in session and 'mobile_number' in session:
		email_address = session['email_address']
		mobile_number = session['mobile_number']

		# Display all records in the customer table

		cursor.execute('SELECT customer_id, first_name, last_name, email_address, mobile_number, age FROM customer')
		customers = cursor.fetchall()

		return render_template('customerModule.html', customers=customers)
	
	return redirect(url_for('login'))

def signupAccount():
	'''Registers a new account.'''

	db = get_db()
	cursor = db.cursor()

	try:
		# Get the user input for all fields 

		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email_address = request.form['email_address']
		mobile_number = request.form['mobile_number']
		age = request.form['age']

		# Query a customer record using the inputted email and number

		cursor.execute('SELECT customer_id FROM customer WHERE email_address=%s OR mobile_number=%s', (email_address, mobile_number))
		row = cursor.fetchone()

		# Check if the account already exists 
		# If the account does not exist yet, insert it into the database, otherwise, flash an error message

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

def loginAccount():
	'''Logs in an account.'''

	db = get_db()
	cursor = db.cursor()

	try:
		# Get the user input for the email and number fields

		email_address = request.form['email_address']
		mobile_number = request.form['mobile_number']

		# Query a customer record using the inputted email and number

		cursor.execute('SELECT customer_id FROM customer WHERE email_address=%s AND mobile_number=%s', (email_address, mobile_number))
		row = cursor.fetchone()

		# If the account already exists, route it to the movie selection page, otherwise, flash an error message

		if row:
			flash('Found account', 'info') # This message is for checking only, replace with code to route to the movie selection page 
		else:
			flash('Account does not exist', 'error')
	except mysql.connector.Error as e:
		pass
	finally:
		cursor.close()
		db.close()

if __name__ == '__main__':
	app.run(debug=True)