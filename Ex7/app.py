from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def main():
    return 'Hello WEB class main'

@app.route('/joke')
def jokking():
    return 'A man walks into a bar, takes a look around and says "Hello World!" '

@app.route('/hello')
def hi():
    return redirect('/joke')


@app.route('/backTo')
def goMain():
 return redirect(url_for('main'))


if __name__ == '_main_':
    app.run(debbug=True)