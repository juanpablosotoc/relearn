from flask import Flask, render_template, request, redirect
import os
from mysql_jp import mysql_decorate


app = Flask(__name__)
app.secret_key = os.getenv('relearn_flask_key')


@mysql_decorate
def create_user(connection, cursor, **kwargs):
	query = f"""
	INSERT INTO users (email, password)
	VALUES ('{kwargs['email']}', '{kwargs['password']}')
	"""
	cursor.execute(query)
	connection.commit()

@mysql_decorate
def update_cv_db(connection, cursor, **kwargs):
	query = f"""
	UPDATE users 
	set costo={kwargs['costos']}, venta={kwargs['ventas']}
	where id={kwargs['id']}
	"""
	cursor.execute(query)
	connection.commit()

@mysql_decorate
def get_data(connection, cursor, **kwargs):
	query = f"""
	SELECT *
	FROM users
	WHERE email='{kwargs['email']}'
	"""
	cursor.execute(query)
	return cursor.fetchall()
	

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('/index.html')
	else: 
		usr_data = get_data.connect(email=request.form['email'])['data']
		if len(usr_data) == 0 or usr_data[0]['password'] != request.form['password']:
			return render_template('/index.html')
		else:
			return redirect(f'/data/{usr_data[0]["email"]}')


@app.route('/create-user', methods=['GET', 'POST'])
def create_user_endp():
	if request.method == 'GET':
		return render_template('/create_user.html')
	else:	
		result = create_user.connect(email=request.form['email'], password=request.form['password'])
		if result['error']:
			return render_template('/create_user.html')
		else: 
			return redirect(f'/data/{request.form["email"]}')


@app.route('/data/<email>', methods=['GET', 'POST'])
def data(email):
	if request.method == 'GET':
		usr_data = get_data.connect(email=email)['data'][0]
		return render_template('/data.html', costos=usr_data['costo'], ventas=usr_data['venta'], email=email)
	else:
		usr_id = get_data.connect(email=email)['data'][0]['id']
		update_cv_db.connect(id=usr_id, ventas=request.form['ventas'], costos=request.form['costos'])
		return redirect(f'/data/{email}')


if __name__ == '__main__':
	app.run()

