#!/usr/bin/env python

import flask
import flask_socketio

'''
socketio.run() function encapsulates the start up of the web server and
replaces the standard app.run()
'''
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = flask_socketio.SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)
