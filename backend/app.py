from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data),200

if __name__ == '__main__':
    app.run(debug=True,host='')
    
    

