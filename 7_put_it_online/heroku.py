from bottle import route, run, os


# This server does not run locally. It is designed to be run on Heroku.

@route('/')
def index():
    return 'Hello world! I run on Heroku!'


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
