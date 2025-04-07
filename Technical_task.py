from flask import Flask, request, render_template_string, redirect
import sqlite3

app = Flask(__name__)

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name and email:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            conn.close()
            message = "Form submitted successfully!"
        else:
            message = "Please fill all fields."

    return render_template_string('''
    <h2>User Form</h2>
    <form method="POST">
        <input name="name" placeholder="Name"><br><br>
        <input name="email" placeholder="Email"><br><br>
        <input type="submit" value="Submit">
    </form>
    <p>{{message}}</p>
    ''', message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
