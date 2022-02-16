from flask import Flask, jsonify


app = Flask(__name__)

from cow import cow

@app.route('/ping')

def ping():
    return jsonify({"mensaje":"pong"})

@app.route('/cow')

def getCows():
    return jsonify({"cow":cow, "mensaje":"lista de vacas"})

@app.route('/cow/<string:cow_id>')
def getCow(cow_id):
    cow_found=[cow for cow in cow if cow['id']==cow_id]
    if (len(cow_found)>0):
        return jsonify(cow_found[0])
    return jsonify({"mensaje": "Vaca no encontrada"})



if __name__=='__main__':
    app.run(debug=True, port=4000)