from flask import *
import secrets
import requests
app = Flask(__name__)

@app.route('/API/', methods=['GET','POST'])
def get():
        msg= request.args.get('username')
        url_id = f'https://www.instagram.com/{msg}/?__a=1'
        cookie  = secrets.token_hex(8)*2
        head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': cookie,
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With": "XMLHttpRequest",
"X-IG-App-ID" : "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
        }
        req_id = requests.get(url_id,headers=head).text
        if 'graphql' in req_id:
         url_id = f'https://www.instagram.com/{msg}/?__a=1'
         cookie  = secrets.token_hex(8)*2
         head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': cookie,
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With": "XMLHttpRequest",
"X-IG-App-ID" : "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
        }
         req_id = requests.get(url_id,headers=head).json()
         bio = str(req_id['graphql']['user']['biography'])
         nam = str(req_id['graphql']['user']['full_name'])
         idd = str(req_id['graphql']['user']['id'])
         isp = str(req_id['graphql']['user']['is_private'])
         isv = str(req_id['graphql']['user']['is_verified'])
         pro = str(req_id['graphql']['user']['profile_pic_url'])
         data = {'bio': f'{bio}' , 'name': f'{nam}', 'id': f'{idd}','user': f'{msg}','private': f'{isp}', 'verified' :f'{isv}'}
         return data
        else:
         da={"Eroor":'Server'}
         return da
        
