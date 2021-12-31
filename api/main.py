import flask
import requests
from flask import *
app=Flask(__name__)
@app.route("/")
def Hom():
 sd={'erorr': 'url'}
 return sd
@app.route("/api/")
def Home():
        users= request.args.get('username')
        for w in users:
         url = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.20638847989925613&include_reel=true"
         response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}).json()['users']
         us=[]
         for ig in response:
          user = ig['user']['username']
          us.append(user)
          print(user)
         else:
          data =  {'data': us , 'KaRloS': '200'}
          print(data)
          return data
