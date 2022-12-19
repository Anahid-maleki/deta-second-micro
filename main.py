from flask import Flask,render_template,jsonify
import requests ,json
#import os
#my_key=os.environ.get('API_key')
#response=requests.get("https://api.github.com/users")
app=Flask(__name__)
@app.route('/<username>',methods=['GET'])
def Hello_User(username):
    return f"<html><body>Hello and Welcome {username}....</body></html>"
@app.route('/home',methods=['GET'])
def home():
    return render_template("text.html") 
 
#@app.route("/",methods=["GET"])
#def get_info():
#    url="https://api.github.com/users/Anahid-maleki"
    # response=requests.get(url,headers={'my_token': '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'})
    # jsonData=response.json()
    # return jsonify(jsonData['id'])
    

      
