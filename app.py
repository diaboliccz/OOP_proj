from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from User import UserDatabase, User, Admin
from verification import *
app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

user_database = UserDatabase()

# Dummy data for testing purposes
user_database.add_user(User(user_database, None, 'user1', 'password1', 'user1@example.com', '1234567890', 'User One'))
user_database.add_user(Admin(user_database, None, 'admin1', 'password1', 'admin1@example.com', '1234567890', 'Admin One'))

@login_manager.user_loader
def load_user(user_id):
    return user_database.get_user(user_id)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_database.login(username, password)
        if user:
            login_user(user)
            send_verification_email(user)
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/verify', methods=['GET', 'POST'])
@login_required
def verify():
    if request.method == 'POST':
        token = request.form['token']
        if token == str(current_user.__email_verification_token):
            return 'Your email has been verified!'
        else:
            return 'Invalid verification code'
    return render_template('verify.html')


if __name__ == '__main__':
    app.run(debug=True)
