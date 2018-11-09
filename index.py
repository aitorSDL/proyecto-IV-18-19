from flask import Flask

app = Flask(__name__)
PORT=5000
DEBUG=False


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/productos')
def comparacion():
    return 'Hello, pepo!'

@app.route('/login')
def comparacion():
    return 'Hello, sam!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =  PORT, debug = DEBUG)
