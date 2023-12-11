from flask import Flask, render_template, request, redirect
import sqlite3
from urllib.parse import quote  

app = Flask(__name__)

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        designation TEXT,
        salary REAL,
        dob TEXT,
        address TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return render_template('index.html', employees=employees, quote=quote)  # Pass quote function to template

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        designation = request.form['designation']
        salary = request.form['salary']
        dob = request.form['dob']
        address = request.form['address']

        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employees (name, department, designation, salary, dob, address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, department, designation, salary, dob, address))
        conn.commit()
        conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
