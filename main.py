from flask import Flask,render_template
import requests
from dotenv import load_dotenv
import json
import os

my_key=os.environ.get('API_key')
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
@app.route("/info")
def get_info():
    url="https://api.github.com/users/Anahid-maleki"
    response=requests.get(url,headers={'athorization':"token{}".format(my_key)})
    for x in response.json():
       return {x["name"]}
