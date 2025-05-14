from flask import Flask, render_template, request, redirect, url_for, session
from app_logic import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

# Dummy user for demo
users = {'admin': 'password123',
         'hr':'password123'}

@app.route('/')
def home():
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password and username == 'admin': #determines the dashboard being POST-ed
            session['user'] = username
            return redirect(url_for('dashboard_user'))
        elif username in users and users[username] == password and username == 'hr': #if they are a part of hr
            session['user'] = username
            return redirect(url_for('dashboard_hr'))
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

@app.route('/dashboard_hr')
def dashboard_hr():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard_hr.html', user=session['user'])

@app.route('/referral_creation', methods=['GET', 'POST'])
def referral_creation():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        referral_subject = request.form.get('user_referral_subject')
        referral_notes = request.form.get('user_notes')

    return render_template('referral_creation.html', user=session['user'])

@app.route('/view_referral')
def view_referral():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('view_referral.html', user=session['user'])

if __name__ == '__main__':
    app.run(debug=True)