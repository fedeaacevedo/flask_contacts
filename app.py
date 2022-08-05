
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'administrador'
app.config['MYSQL_DB'] = 'flask_contacts'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute(
                "INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('index'))

@app.route('/edit')
def edit_contact():
    return 'editar'

@app.route('/delete')
def delete_contact():
    return 'delete'

if __name__ == '__main__':
    app.run(port=3000, debug=True)