from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database" for demonstration purposes
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        idno = request.form['idno']
        password = request.form['password']
        # Check if user exists
        for user in users:
            if user['idno'] == idno and user['password'] == password:
                return redirect(url_for('home'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'idno': request.form['idno'],
            'lastname': request.form['lastname'],
            'firstname': request.form['firstname'],
            'midname': request.form['midname'],
            'course': request.form['course'],
            'yearlevel': request.form['yearlevel'],
            'email': request.form['email'],
            'username': request.form['username'],
            'password': request.form['password']
        }
        users.append(user_data)
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)