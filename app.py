from flask import Flask, render_template, request, redirect, url_for, session
from app_logic import *
from database_module import database_manager
from env_module import get_conn_string
from email_module import email_manager

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

@app.route('/')
def home():

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = database_manager(get_conn_string())
        session['user'] = db.get_user_by_email(email)
        session['referrals'] = db.get_all_referrals()
        db.close_connection()

        if password == session['user']['pass']:
            if session['user']['dept_id'] != 1:
                return redirect(url_for('dashboard_user'))
            else:
                return redirect(url_for('dashboard_hr'))
        
        # diction = { #a dictionary based on user data
        #             'id': userid,
        #             'dept_id' : departmentid,
        #             'name': full_name,
        #             'email': email,
        #             'pass': password
        #         }

        # diction = {
        #                 'ref': referralid,
        #                 'userid': user_id,
        #                 'departmentid': departmentid,
        #                 'ref_sub': ref_subject,
        #                 'user_notes': usr_notes,
        #                 'hr_notes': hr_notes,
        #                 'confidential': confidential,
        #                 'expense': expense
        #             }

        
        # if username in users and users[username] == password and username == 'admin': #determines the dashboard being POST-ed
        #     session['user'] = username
        #     return redirect(url_for('dashboard_user'))
        # elif username in users and users[username] == password and username == 'hr': #if they are a part of hr
        #     session['user'] = username
        #     return redirect(url_for('dashboard_hr'))
        return "Invalid credentials! Please Refresh the page to try again!"
    return render_template('login.html')

@app.route('/dashboard_user')
def dashboard_user():
    if 'user' not in session:
        return redirect(url_for('login'))

    # Simulated list of referral dictionaries
    referrals = []

    all_ref = session['referrals']

    for ref in all_ref:
        if ref['userid'] == session['user']['id']:
            referrals.append(ref)

    #valid_confidential_count = sum(1 for r in referrals if r['confidential'] in ['True', 'False'])
    total = len(referrals)

    return render_template(
        'dashboard_user.html',
        user=session['user'],
        referrals=referrals,
        # complete=valid_confidential_count,
        total=total
    )

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

        db = database_manager(get_conn_string())

        ref = session['referrals']
        user = session['user']
        db.insert_new_referral((len(ref) + 1), user['id'], user['dept_id'], referral_subject, referral_notes, 
                               "", 1, "None")

        db.close_connection()

        email = email_manager(user['email'])
        email.get_email_submission(user['name'], user['dept_id'], referral_subject)

    #diction = { #a dictionary based on user data
        #             'id': userid,
        #             'dept_id' : departmentid,
        #             'name': full_name,
        #             'email': email,
        #             'pass': password
        #         }

    return render_template('referral_creation.html', user=session['user'])

@app.route('/view_referral')
def view_referral():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('view_referral.html', user=session['user'])

if __name__ == '__main__':
    app.run(debug=True)