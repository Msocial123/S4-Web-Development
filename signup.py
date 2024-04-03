from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for user authentication (replace this with your actual user authentication mechanism)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success', username=username))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/success/<username>')
def success(username):
    return f'<h1>Welcome, {username}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
