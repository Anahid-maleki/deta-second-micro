from flask import Flask,render_template
import requests
response=requests.get("https://api.github.com/User")
app=Flask(__name__)
@app.route('/<username>',methods=['GET'])
def Hello_User(username):
    return f"<html><body>Hello and Welcome {username}....</body></html>"
@app.route('/home',methods=['GET'])
def Home():
    return render_template("text.html") 
@app.route("/get user",methods=['GET'])
def user_github():
    return f"{response.json}"    
