from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Simple Flask App!"

# Route to render the add page with a form
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
            success_message = "Success! The answer is calculated."
            return render_template('add.html', result=result, success_message=success_message)
        except (ValueError, TypeError):
            error_message = "Please enter valid numbers."
            return render_template('add.html', error_message=error_message)
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
