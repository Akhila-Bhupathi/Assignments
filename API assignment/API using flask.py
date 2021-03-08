from flask import Flask,request,jsonify
app=Flask(__name__)

notes_list=[
    {
        "id":1,
        "title":"class",
        "description":"At 9 AM",
    },
    {
        "id":2,
        "title":"Assignment",
        "description":"Deadline is on saturday",
    },
    {
        "id":3,
        "title":"movie",
        "description":"Movie booking",
    },
    {
        "id":4,
        "title":"project",
        "description":"Discuss about database",
    }
]

@app.route('/notes',methods=['GET','POST'])
def notes():
    if request.method=='GET':
        if len(notes_list)>0:
            return jsonify(notes_list)
        else:
            "Empty",404
        
    if request.method=='POST':
        new_title=request.form['title']
        new_description=request.form['description']
        new_id=notes_list[-1]['id']+1

        new_notes={
            "id":new_id,
            "title":new_title,
            "description":new_description
        }

        notes_list.append(new_notes)
        return jsonify(notes_list),201

@app.route('/notes/<int:id>')
def get_notes(id):
    for notes in notes_list:
        if(notes['id'])==id:
            return jsonify(notes)
    return jsonify({"message":"not found"})

if __name__=='__main__':
    app.run()