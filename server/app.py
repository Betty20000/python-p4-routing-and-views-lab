#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return f'{parameter}'
@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(num) for num in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')  
def math(num1, operation, num2):
    if operation == '+':
        print(str(num1 + num2))
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1/num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return('Errror: Invalid Operator')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
