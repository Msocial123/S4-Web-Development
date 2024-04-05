from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials
users = {'john': 'password123', 'emma': 'abc123'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        # Redirect to a dashboard or some other page after successful login
        return redirect(url_for('dashboard'))
    else:
        error = 'Invalid username or password. Please try again.'
        return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
