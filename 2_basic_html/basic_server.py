from bottle import route, run, template


@route('/')
def index():
    return template('basic_html')


run(host='localhost', port=8080)
