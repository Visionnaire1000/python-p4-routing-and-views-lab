from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    return "<br>".join(str(i) for i in range(1, number + 1))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2) if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(debug=True)
