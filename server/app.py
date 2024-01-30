#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print (string)
    return f'{string}'

@app.route('/count/<int:number>')
def count(number):
    output = ''
    for i in range(number):
        output += str(i) + "\n"
    return output

@app.route('/math/<int:num1>/<oper>/<int:num2>')
def math(num1, oper, num2):
    res = None
    if oper == '+':
        res=num1+num2
    elif oper == '-':
        res=num1-num2
    elif oper == '*':
        res=num1*num2
    elif oper == 'div':
        res=num1/num2
    elif oper == '%':
        res=num1%num2
    return str(res)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
