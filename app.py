from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

# Dummy user for demo
users = {'Tyler': 'password123'}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard_user'))
        return "Invalid credentials!"
    return render_template('login.html')

@app.route('/dashboard_user')
def dashboard_user():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard_user.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 