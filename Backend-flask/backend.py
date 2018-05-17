from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import models as dbHandler
from flask import redirect



app=Flask(__name__)
app = Flask(__name__, static_url_path='/static')



@app.route('/')
def home():
	return render_template('index.html')
	#url_for('static', filename ='styles.css')


@app.route('/registrar', methods= ['GET', 'POST'])
def registro():
	return render_template('registrar.html')


	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		dbHandler.insertUser(username, password)
		users = dbHandler.retrieveUsers()

		return render_template('index.html', users=users)
	else:
		return render_template('registrar.html')



@app.route('/formulario', methods=['GET', 'POST'])
def login():
	return render_template('formulario.html')

	
	

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

	return redirect(url_for('home'))
if __name__=='main':
	app.run(use_reloader=True, debug=True)