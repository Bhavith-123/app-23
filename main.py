from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('app', 'user'))

@app.route('/app/user')
def home_page():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
