from flask import Flask, request, render_template, make_response
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('phone_number.html')


@app.route('/url_arg')
def url_arg():
    return render_template('url_arg.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookie')
def cookie():
    resp = make_response(render_template('cookie.html'))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user','NoName')
    return resp

@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html' )

@app.route('/calculator')
def calculator():
    result = ''
    num1 =  request.args.get('num1') 
    oper = request.args.get('operation') 
    num2 = request.args.get('num2')
    if oper == "+": 
        result = int(num1)+ int(num2)
    elif oper == "-":
        result = int(num1) - int(num2)
    elif oper == "*":
        result = int(num1) * int(num2)
    elif oper == "/":
        result = int(num1)/int(num2)
    return render_template('calculator.html', result=result)

@app.route('/phone_number', methods=['POST'])
def phone_number():
    phone_number = request.form['phone_number']

    error_message = None
    success_message = None
    formatted_phone = None

    # Проверка на допустимые символы
    if not re.match(r'^[0-9 ()\-.+]+$', phone_number):
        error_message = 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'
    else:
        # Удаляем все символы, кроме цифр
        cleaned_phone = re.sub(r'[^\d]', '', phone_number)

        # Проверка длины номера
        if len(cleaned_phone) == 10 or (len(cleaned_phone) == 11 and (cleaned_phone.startswith('8') or cleaned_phone.startswith('7'))):
            # Форматирование номера
            formatted_phone = f'8-{cleaned_phone[0:3]}-{cleaned_phone[3:6]}-{cleaned_phone[6:8]}-{cleaned_phone[8:10]}'
            success_message = 'Номер успешно проверен и отформатирован.'
        else:
            error_message = 'Недопустимый ввод. Неверное количество цифр.'

    return render_template('phone_number.html', error_message=error_message, success_message=success_message, formatted_phone=formatted_phone)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, make_response
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('phone_number.html')


@app.route('/url_arg')
def url_arg():
    return render_template('url_arg.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookie')
def cookie():
    resp = make_response(render_template('cookie.html'))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user','NoName')
    return resp

@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html' )

@app.route('/calculator')
def calculator():
    result = ''
    num1 =  request.args.get('num1') 
    oper = request.args.get('operation') 
    num2 = request.args.get('num2')
    if oper == "+": 
        result = int(num1)+ int(num2)
    elif oper == "-":
        result = int(num1) - int(num2)
    elif oper == "*":
        result = int(num1) * int(num2)
    elif oper == "/":
        result = int(num1)/int(num2)
    return render_template('calculator.html', result=result)

@app.route('/phone_number', methods=['POST'])
def phone_number():
    phone_number = request.form['phone_number']

    error_message = None
    success_message = None
    formatted_phone = None

    # Проверка на допустимые символы
    if not re.match(r'^[0-9 ()\-.+]+$', phone_number):
        error_message = 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'
    else:
        # Удаляем все символы, кроме цифр
        cleaned_phone = re.sub(r'[^\d]', '', phone_number)

        # Проверка длины номера
        if len(cleaned_phone) == 10 or (len(cleaned_phone) == 11 and (cleaned_phone.startswith('8') or cleaned_phone.startswith('7'))):
            # Форматирование номера
            formatted_phone = f'8-{cleaned_phone[0:3]}-{cleaned_phone[3:6]}-{cleaned_phone[6:8]}-{cleaned_phone[8:10]}'
            success_message = 'Номер успешно проверен и отформатирован.'
        else:
            error_message = 'Недопустимый ввод. Неверное количество цифр.'

    return render_template('phone_number.html', error_message=error_message, success_message=success_message, formatted_phone=formatted_phone)


if __name__ == '__main__':
    app.run(debug=True)
