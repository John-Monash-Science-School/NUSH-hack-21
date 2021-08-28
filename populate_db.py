import random
import json
import sqlite3
import requests
from hashlib import sha256
from nonroutes import gen_hash

def sql_handler(function):
    def wrapper(*args,**kwargs):
        conn = sqlite3.connect('./nush.db')
        cursor = conn.cursor()
        output = function(*args,curs=cursor,**kwargs)
        conn.commit()
        conn.close()
        return output
    wrapper.__name__ = function.__name__
    return wrapper

@sql_handler
def generate(size,curs):
    r = requests.get(f'https://randomuser.me/api/?results={size}&inc=login,picture')
    data = r.json()['results']
    for person in data:
        pass1 = 'password'

        #generate a salt and the hashes
        salt = str(random.randint(10**5,10**6))
        hash = gen_hash(pass1, salt)

        username = person['login']['username']
        pfp = person['picture']['thumbnail']

        #create user
        curs.execute('INSERT INTO users (username,password,salt,coins,image_link) VALUES (?,?,?,0.00,?)',(username,hash,salt,pfp))

generate(50)