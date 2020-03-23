from flask import Flask , request , jsonify

app = Flask(__name__)

person = [
    {
        'id' : '5935512007',
        'name' : 'Donnukrit',
        'surname': 'Satirakul',
        'faculty': 'Engineering',
    }
]
@app.route('/',methods=['GET'])
def Hello() :
    return "Hello World"

@app.route('/api/person',methods=['GET'])
def showPerson():
    return jsonify(person)

app.run(debug=[True])