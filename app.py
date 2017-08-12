from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password4$'
app.config['MYSQL_DATABASE_DB'] = 'student_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')#root location
def hello_world():
    return 'Hello, World!'

@app.route('/teacher')#root location
def home():
    return render_template("home.html")

@app.route('/student')
def student():
    return render_template("student.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)