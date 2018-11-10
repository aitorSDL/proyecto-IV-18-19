from flask import Flask , render_template


app = Flask(__name__)
PORT=5000
DEBUG=False


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/productos')
def comparacion():
    return 'Hello, soy una nvidia gtx!s'

@app.route('/login')
def comparacion(): 
    return 'Hello, sam!'  


if __name__ == '__main__':
    app.run( port =  PORT, debug = DEBUG)
