from flask import Flask, render_template


app = Flask(__name__)
PORT=5000
DEBUG=False


@app.route('/')
def index():
    return render_template('hola_world.html', user=user)

@app.route('/productos')
def comparacion():
    return 'Hello, soy una nvidia gtx! '

if __name__ == '__main__':
    app.run( port =  PORT, debug = DEBUG)
