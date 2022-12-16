from flask import Flask
app=Flask(__name__)
@app.route('/<username>',methods=['GET'])
def Hello_User(username):
    return f"<html><body>Hello and Welcome {username}....</body></html>"
@app.route('/home',methodes=['GET'])
def Home():
    return render_template("text.html")    
    