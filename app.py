from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/order/')
def order():
    return render_template('order.html')
@app.route('/account/')
def account():
    return render_template('account.html')
if __name__ == "__main__":
    app.run(debug=True)