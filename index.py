from flask import Flask, render_template, request


app = Flask(__name__)
PORT=5000
DEBUG=False


@app.route('/')
def index():
    return 

@app.route('/', methods = ['GET'])
def status():
    render_template('base.html')
    response =  {"status" : "OK"}
    return jsonify(response);

@app.route('/status', methods = ['GET'])
def status():
    
    response =  {"status" : "OK",
                 "web_status" :
                    {
                     "total" : 10,
                     "productos" : 20,
                     
                     }
                 }
    return jsonify(response);


@app.route('/productos')
def comparacion():
    return 'Hello, soy una nvidia gtx! '

if __name__ == '__main__':
    app.run( port =  PORT, debug = DEBUG)
