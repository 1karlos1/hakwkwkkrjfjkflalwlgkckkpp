import requests
from bs4 import BeautifulSoup
import requests,json,flask
from flask import Flask,jsonify
from flask import *
app = Flask(__name__)
@app.route('/api/')
def hi():
    user= request.args.get('user')
    def get_data(user):
        data, last_posts, user_data, = [], [], {}
        user_data_keys = ['posts', 'followers', 'following']
        url = requests.get(f'https://greatfon.com/v/{user}')
        src = url.content
        soup = BeautifulSoup(src, "html.parser")
        get_data = soup.find_all("li", {"class": "user__item"})
        get_posts = soup.find_all('img', {"class": "content__img"})
        for i in range(len(get_data)):
            data.append(get_data[i].text)
        for i in range(len(get_posts)):
            last_posts.append(get_posts[i].attrs['src'])

        c = 0
        for i in data:
            user_data[user_data_keys[c]] = str(i).rsplit(' ',1)[0].replace(' ','')
            c += 1

        return user_data,last_posts

    def get_adv_data(user,type):

        data = []
        url = requests.get(f'https://greatfon.com/v/{user}/{type}')
        src = url.content
        soup = BeautifulSoup(src, "html.parser")
        get_followers = soup.find_all('h6')
        for i in range(len(get_followers)):
            data.append(get_followers[i].text)
        print(' Scraping data...')
    try:
        data = get_data(user)[0]     # posts / followers / following ( in dict )
        adv = get_data(user)[1]      # last posts ( in list )
        followers_list = get_adv_data(user,'followers')     # last followers ( in list )
        following_list = get_adv_data(user,'following')     # last following ( in list )
        followers, posts, following = data['followers'], data['posts'], data['following']
        return {'followers':followers,'following':following,'posts':posts}
    except:
        return {'user':'user not fond'}
        
