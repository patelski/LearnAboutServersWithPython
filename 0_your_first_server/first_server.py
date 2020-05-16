import os
from bottle import route, run


@route('/helloworld')
def index():
    return 'Hello world!'


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
