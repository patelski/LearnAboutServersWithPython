import os
from bottle import route, run


@route('/helloworld')
def index():
    return 'Hello world!'


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
