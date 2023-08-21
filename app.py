from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Gaurav@123"
app.config['MYSQL_DB'] = "ibm"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['subject']
        email = request.form['email']
        message = request.form['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact_me (name,subject,email,message) VALUES (%s,%s,%s,%s)", (name, subject, email, message))
        mysql.connection.commit()
        cur.close()
        return "Thank you for Contact Me."

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)