from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '1234'

USER_DB = [
    {'id': 1, 'name': 'gildong', 'email': 'gildong@hwalbin.dang'},
    {'id': 2, 'name': 'gwansun', 'email': 'gwansun@manse.com'}
]

@app.route('/')
def index():
    if 'user_id' in session:
        user = next((user 
                        for user in USER_DB 
                            if user['id'] == session['user_id']), 
                    None)
    else:
        user = None
    return render_template('index.html', users=USER_DB, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = next((user for user in USER_DB if user['email'] == email), None)
        if user:
            session['user_id'] = user['id']
            session['user_password'] = user['password']
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_password', None)
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if 'user_id' and 'user_password' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_id = len(USER_DB) + 1
        name = request.form['name']
        email = request.form['email']
        USER_DB.append({'id': new_id, 'name': name, 'email': email})
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = next((user for user in USER_DB if user['id'] == user_id), None)
    if request.method == 'POST':
        if user:
            user['name'] = request.form['name']
            user['email'] = request.form['email']
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    global USER_DB
    USER_DB = [user for user in USER_DB if user['id'] != user_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)