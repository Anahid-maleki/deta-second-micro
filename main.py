from flask import Flask,render_template,jsonify 
import requests
from dotenv import load_dotenv
load_dotenv()
#import json
import os
password=os.getenv("my_token")
#my_key=os.environ.get('API_key')
#response=requests.get("https://api.github.com/users")
app=Flask(__name__)
# @app.route('/<username>',methods=['GET'])
# def Hello_User(username):
#     return f"<html><body>Hello and Welcome my friend {username}....</body></html>"
@app.route('/home',methods=['GET'])
def home():
    return render_template("text.html") 
 
@app.route("/<username>",methods=["GET"])
def get_info(username):
   url="https://api.github.com/users"
   final_url= '/'.join([url, username])
   response=requests.get(final_url,headers={"my_token":"password"})
   jsonData=response.json()
   return jsonify(jsonData)
    

      
