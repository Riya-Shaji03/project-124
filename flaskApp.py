from flask import Flask,jsonify, request

app=Flask(__name__)
tasks=[
    {
        
        "contact":u"9437942016",
        "Name":u"Ronald",
        'done': False,
        'id': 1,
    },
    {
        
        "contact":u"73406251082",
        "Name":u"Stacy",
        "done": False,
        "id": 2,
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add_data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    contact={
        "id":tasks[-1]['id']+1,
        'Name':request.json['Name'],
        "contact": request.json.get('contact',""),
        'done':False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message":"Data added successfully"
    })

@app.route("/get_data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)