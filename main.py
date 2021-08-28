from flask import Flask, request, url_for, render_template, make_response, Markup
from flask_socketio import SocketIO, join_room, leave_room
from nonroutes import *
import random
import json
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True if __name__ == '__main__' else False
socketio = SocketIO(app)

#this is a decorator that handles all of the construction and teardown of sql connections
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
def verify_user(request,curs):
    #get cookie
    userID = request.cookies.get('userID')
    salt = request.cookies.get('salt')

    #check cookie exists
    if not userID or not salt:
        return False

    #check it matches db
    curs.execute('SELECT salt FROM users where username=?',(userID,))
    dbsalt = curs.fetchone()
    return dbsalt != None and dbsalt[0] == salt

#this one is just for heroku
def create_app():
    global app
    return app

# beep boop socket examples
# in js: 
#    let socket = io.connect('http://' + document.domain + ':' + location.port);
#    socket.on('event', function(data) {
#        console.log('queue change!')
#    });
@socketio.on('event')
def socket_event(code, more_args): 
    # socketio.emit('event', dict_data, room=code, broadcast=True)
    pass

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/usertest')
@sql_handler
def usertest(curs):
    logged_in = verify_user(request)
    
    if not logged_in:
        return "<script>window.location = './login'</script>"
    return "you're logged in!"

@app.route('/login',methods=["GET","POST"])
@sql_handler
def login(curs):
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #get data from db
        username = request.form['user']
        password = request.form['password']
        curs.execute('SELECT * FROM users WHERE username=?',(username,))
        user = curs.fetchone()

        #check user exists
        if not user:
            return 'that user does not exist'

        #generate hashed password
        salt = user[2]
        hash = gen_hash(password,salt)

        #check password
        if hash != user[1]:
            return 'wrong password!'
        
        resp = make_response('Logged in!')
        #lol this is garbage securitywise
        resp.set_cookie('userID', username)
        resp.set_cookie('salt', salt)
        return resp

@app.route('/signup',methods=["GET","POST"])
@sql_handler
def signup(curs):
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        #verify passwords match
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        if pass1 != pass2:
            return "silly bugger, the passwords don't match"

        #see if username is unique
        username = request.form['user']
        curs.execute('SELECT * FROM users WHERE username=?',(username,))
        user = curs.fetchone()
        if user != None:
            return "that username is taken lol"

        #generate a salt and the hashes
        salt = str(random.randint(10**5,10**6))
        hash = gen_hash(pass1, salt)

        #create user
        curs.execute('INSERT INTO users (username,password,salt,coins) VALUES (?,?,?,0.00)',(username,hash,salt))

        return "user created!"

@app.route('/account/<username>',methods=["GET","POST"])
@sql_handler
def account(username,curs):
    #check if logged in
    logged_in = verify_user(request)
    if not logged_in:
        return "<script>window.location = './login'</script>"
    
    #check if this is the users account
    ownpage = False
    userID = request.cookies.get('userID')
    if userID == username:
        ownpage = True
    
    #get user info
    curs.execute('SELECT coins FROM users WHERE username = ?',(username,))
    coins = curs.fetchone()
    if not coins:
        return "that's not a real account lol"
    coins = str(round(coins[0], 2))

    print(ownpage)

    return render_template('account.html',coins=coins,ownpage=ownpage,username=username)

@app.route('/calculator')
def calculator():
    return render_template('calculate.html')

@app.route('/search')
@sql_handler
def search(curs):
    #actually search
    username = request.form.get('username')
    results = None
    searched = False
    if username:
        curs.execute('SELECT username FROM users WHERE username LIKE ?',(username,))
        results = curs.fetchall()
        searched = True
    return render_template('search.html',results=results,searched=searched)

### COMPONENTS FOR PREACT, IF USED ####
@app.context_processor
def component_processor():
    def component_import(*args):
        output_str = ""
        for i in args:
            f = open(f"./components/{i}.js", "r")
            f_str = f.read()
            output_str += f"{f_str}\n"
        return Markup(output_str)
     
    return dict(component_import=component_import)

if __name__ == '__main__':
    @app.route('/debug')
    def debug():
        0/0
    socketio.run(create_app(),host='0.0.0.0')