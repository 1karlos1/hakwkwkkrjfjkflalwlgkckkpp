import requests,json,flask
from flask import Flask,jsonify
from flask import *
from user_agent import generate_user_agent
app = Flask(__name__)
@app.route('/api/')

def swap():
	sessionid1 = request.args.get('co')
	username_target = request.args.get('user')
	while True:
                url_check_username_available_or_no = f'https://www.instagram.com/{username_target}/'
                headers_username_target = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': f'ig_did=DD8FB38A-099F-48A1-AFB1-C20260E1757F; mid=YC6rLwAEAAG0k1JKnzMvffDxbZGb; ig_nrcb=1; csrftoken=jXEakypxebYg4zJjig42oORyMFc9mSbH; rur=ATN; ds_user_id=45913171547; sessionid={sessionid1}',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
                }
                req_check_user = requests.get(url_check_username_available_or_no, headers=headers_username_target).status_code
                if req_check_user == 404:
                    url_your_data = 'https://www.instagram.com/accounts/edit/?__a=1'
                    headers_your_data = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                        'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; ds_user_id=45334757205; rur=VLL; csrftoken=bIgRYPpWJicGXzVLzCoHrxzy0NCe0VJs; sessionid={sessionid1}',
                        'referer': 'https://www.instagram.com/accounts/edit/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                        'x-ig-app-id': '936619743392459',
                        'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9KR4',
                        'x-requested-with': 'XMLHttpRequest'
                    }
                    data_your_data = {
                        '__a': '1'
                    }
                    req_your_data = requests.get(url_your_data, data=data_your_data, headers=headers_your_data)
                    email = str(req_your_data.json()['form_data']['email'])
                    phone_number = str(req_your_data.json()['form_data']['phone_number'])
                    is_email_confirmed = str(req_your_data.json()['form_data']['is_email_confirmed'])
                    is_phone_confirmed = str(req_your_data.json()['form_data']['is_phone_confirmed'])
                    birthday = str(req_your_data.json()['form_data']['birthday'])
                    first_name = str(req_your_data.json()['form_data']['first_name'])
                    biography = str(req_your_data.json()['form_data']['biography'])
                    external_url = str(req_your_data.json()['form_data']['external_url'])
                    url_swap_user = 'https://www.instagram.com/accounts/edit/'
                    headers_swap_user = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-length': '138',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': f'ig_did=DD8FB38A-099F-48A1-AFB1-C20260E1757F; mid=YC6rLwAEAAG0k1JKnzMvffDxbZGb; ig_nrcb=1; csrftoken=jXEakypxebYg4zJjig42oORyMFc9mSbH; rur=ATN; ds_user_id=45913171547; sessionid={sessionid1}',
                        'origin': 'https://www.instagram.com',
                        'referer': 'https://www.instagram.com/accounts/edit/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': generate_user_agent(),
                        'x-csrftoken': 'jXEakypxebYg4zJjig42oORyMFc9mSbH',
                        'x-ig-app-id': '936619743392459',
                        'x-ig-www-claim': 'hmac.AR3Y99_RpK0CT93rF-SlG6N-QGmcMHxOrdOcbi_S2BJgNOO1',
                        'x-instagram-ajax': 'f08288f4f45b',
                        'x-requested-with': 'XMLHttpRequest'
                    }
                    data_swap_user = {
                        'first_name': first_name,
                        'email': email,
                        'username': username_target,
                        'phone_number': phone_number,
                        'biography': '@QYQQQ - @Guuuu on Telegram' ,
                        'external_url': external_url,
                        'chaining_enabled': 'on'
                    }
                    req_swap_user = requests.post(url_swap_user, data=data_swap_user, headers=headers_swap_user)
                    if '"status":"ok"' in req_swap_user.text:
                    	return {'user':'ok'}
                    elif req_swap_user.status_code == 404:
                        return {'user':'14day'}
                    elif req_check_user == 200:
                        return {'user':'wiat'}
        
