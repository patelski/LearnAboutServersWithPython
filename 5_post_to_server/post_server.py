from bottle import run, route, request, template

form = '''
        <form action="/formfiller" method="post">
            Name: <input name="name" type="text" />
            Language: <input name="language" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''


@route('/formfiller')
def login():
    return form


@route('/formfiller', method='POST')
def do_login():
    name = request.forms.get('name')
    language = request.forms.get('language').lower()

    if language == 'french':
        friendly_text = '<p><b>Bonjour {{name}}</b>!</p>'
    elif language == 'dutch':
        friendly_text = '<p><b>Hoi {{name}}</b>!</p>'
    else:
        friendly_text = '<p><b>Hello {{name}}</b>!</p>'

    return template(friendly_text, name=name) + form


run(host='localhost', port=8080)
