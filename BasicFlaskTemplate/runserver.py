"""
This script runs the BasicFlaskTemplate application using a development server.
"""

from os import environ
from BasicFlaskTemplate import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    #0.0.0.0 for container -> above for testing on windows
    HOST = '0.0.0.0'
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)
