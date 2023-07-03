#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

# app.py has a resource available at "/"- cleared adding @app.route('/')  
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>'
                                                                                     
# clear display by setting up return <h1> "Python Operations with Flask Routing and Views" in h1 in browser

@app.route('/print/<string:route>')

# ../Flask application in flask_app.py has a resource available at "/print/<parameter>". 
def print_string(route): 
    print (route)
    return route

# ../Flask application in flask_app.py displays text of route in browser.                                                                                                
# ../Flask application in flask_app.py displays text of route in console. 

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

# ../Flask application in flask_app.py has a resource available at "/count/<parameter>".                                                                                 
# ../Flask application in flask_app.py counts through range of parameter in "/count/<parameter" on separate lines.  

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)

# ../Flask application in flask_app.py has a resource available at "/math/<parameters>"                                                                                 
# ../Flask application in flask_app.py adds parameters in "/math/" resource when operation is "+"

    elif operation == '-':
        return str(num1 - num2)

# ../Flask application in flask_app.py subtracts parameters in "/math/" resource when operation is "-" 

    elif operation == '*':
        return str(num1 * num2)

# /Flask application in flask_app.py multiplies parameters in "/math/" resource when operation is "*"

    elif operation == 'div':
        return str(num1 / num2)
    
# Flask application in flask_app.py divides parameters in "/math/" resource when operation is "div".

    elif operation == '%':
        return str(num1 % num2)
    
# Flask application in flask_app.py finds remainder of parameters in "/math/" resource when operation is "%".
if __name__ == '__main__':
    app.run(port=5555, debug=True)


