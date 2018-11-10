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

@app.route('/liga')
def inicio():
    
    ligas = [['slashdot', 'https://slashdot.org'], 
         ['pythonista', 'https://pythonista.io'], 
         ['cloudevel', 'https://cloudevel.com']]
    
    //return render_template('src/Views/plantilla.html', lista=ligas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =  PORT, debug = DEBUG)
