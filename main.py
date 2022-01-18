from flask import *

app = Flask(__name__)  
 
@app.route('/')  
def index():  
    return redirect(url_for('login'))
 
@app.route('/login')  
def defaultuserlogin():  
    return render_template('login.html')

@app.route('/welcome')  
def welcome():  
    return render_template('index.html')

@app.route('/verify', methods = ['POST'])
def validate():
    username = request.form[username]
    password = request.form[password]
    
    if username == 'admin' and password == 'admin@123':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('login'))

@app.route('/success')
def success ():
     return 'Welcome!!! You are Logged In Successfully'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
