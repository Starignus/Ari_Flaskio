#!/usr/bin/env python

from flask import Flask, render_template
from flask_socketio import SocketIO

'''
socketio.run() function encapsulates the start up of the web server and
replaces the standard app.run()
'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))
    return 'one', 2

if __name__ == '__main__':
    socketio.run(app, debug=True)
