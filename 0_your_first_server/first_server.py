from bottle import route, run


@route('/helloworld')
def index():
    return 'Hello world!'


run(host='localhost', port=8080)
