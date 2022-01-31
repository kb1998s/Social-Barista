from flask import Flask, render_template, url_for

app = Flask(__name__)

#HTML app routes
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/order/')
def order():
    return render_template('order.html')
@app.route('/account/')
def account():
    return render_template('account.html')
@app.route('/submit/')
def submit():
    return render_template('submit.html')
@app.route('/friends/')
def friends():
    return render_template('friends.html')

if __name__ == "__main__":
    app.run(debug=True)