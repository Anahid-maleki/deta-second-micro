from flask import Flask,render_template
app=Flask(__name__)
@app.route('/<username>',methods=['GET'])
def Hello_User(username):
    return f"<html><body>Hello and Welcome {username}....</body></html>"
@app.route('/home',methods=['GET'])
def Home():
    return render_template("text.html")
@app.route('/pic',methods=['GET'])        
def pic():
    return f"<html><body><a<body></html>"    