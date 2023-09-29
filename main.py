from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'roma123'


@app.route('/')
def signup():
    return render_template('signup.html')


@app.route('/signin.html')
def signin():
    return render_template('signin.html')


@app.route('/main.html')
def main():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    conn.close()

    return render_template('main.html', posts=posts)


@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? OR email=?", (username, email))
    existing_user = cursor.fetchone()

    if existing_user:
        flash('Username or email already exists!', 'error')
    else:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        flash('Sign-up successful!', 'success')

    conn.close()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
