from flask import Flask,render_template,requests
import urllib.request, json
import os
#response=requests.get("https://api.github.com/users")
app=Flask(__name__)
@app.route('/<username>',methods=['GET'])
def Hello_User(username):
    return f"<html><body>Hello and Welcome {username}....</body></html>"
@app.route('/home',methods=['GET'])
def home():
    return render_template("text.html") 
#@app.route("/info",methods=['GET'])
#def user_github():
#    return {response.json}  
@app.route("/info/<username>")
def get_info(username):
    url="https://api.github.com/users/<username>"
    response=requests.get(url,headers={'athorization':"token{}".format(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)})
    return f"{response.json}"
