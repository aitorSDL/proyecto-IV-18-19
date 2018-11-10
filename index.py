from flask import Flask


app = Flask(__name__)
PORT=5000
DEBUG=False


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/productos')
def comparacion():
    return 'Hello, soy una nvidia gtx!'

if __name__ == '__main__':
    app.run( port =  PORT, debug = DEBUG)
