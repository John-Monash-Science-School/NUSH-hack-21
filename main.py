from flask import Flask, request, url_for, render_template, make_response, Markup
from flask_socketio import SocketIO, join_room, leave_room
import json
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True if __name__ == '__main__' else False
socketio = SocketIO(app)

#this is a decorator that handles all of the construction and teardown of sql connections
def sql_handler(function):
    def wrapper(*args,**kwargs):
        conn = sqlite3.connect('./main.db')
        cursor = conn.cursor()
        output = function(*args,curs=cursor,**kwargs)
        conn.commit()
        conn.close()
        return output
    wrapper.__name__ = function.__name__
    return wrapper

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
    ...


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
@sql_handler
def login(curs):
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/calculator')
def calculator():
    return render_template('calculate.html')

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