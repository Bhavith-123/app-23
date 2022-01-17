from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return return redirect(url_for('app'))

@app.route('/app')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('user.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
