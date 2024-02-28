from flask import Flask, render_template, request, redirect, url_for
import pyperclip
import random

app = Flask(__name__)

passstr = ""
passlen = 0
notification = ""

def generate_password(length):
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""
    for _ in range(length):
        password += random.choice(pass1)
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    global passstr, passlen, notification
    if request.method == 'POST':
        passlen = int(request.form.get('passlen', 0))
        if passlen < 8 or passlen > 20:
            notification = "The password length must be between 8 and 20."
            passstr = ""
        else:
            passstr = generate_password(passlen)
            notification = ""
        return render_template('index.html', passstr=passstr, notification=notification)
    return render_template('index.html', passstr=passstr, notification=notification)

@app.route('/copy', methods=['POST'])
def copy():
    global passstr
    random_password = passstr
    pyperclip.copy(random_password)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
