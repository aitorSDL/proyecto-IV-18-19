from flask import *


app = Flask(__name__)
PORT=5000
DEBUG=False




@app.route('/')
def index():
    response =  {"status" : "OK"}
    jsonify(response);
    return render_template('base.html')
    
@app.route('/status')
def status():
    
    response =  {"status" : "OK",
                 "tienda status_status" :
                    {
                     "total_productos" : 10,
                     "alive" : 5,
                     
                     }
                 }
    return jsonify(response);


@app.route('/productos')
def comparacion():
    return 'Hello, soy una nvidia gtx! '

if __name__ == '__main__':
    app.run( port =  PORT, debug = DEBUG)
