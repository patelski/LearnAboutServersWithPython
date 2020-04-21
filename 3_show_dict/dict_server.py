from bottle import route, run, template


@route('/showdict')
def index():
    stuff = {'me': 'Stefan', 'city': 'The Hague'}
    return template('dict_template', name='dict_server', stuff=stuff)


run(host='localhost', port=8080)