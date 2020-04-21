from bottle import route, run, template


@route('/loop')
def index():
    items = filldict()
    return template('loopy', name='loopyloop', items=items)


def filldict():
    d = dict()
    for number in range(20):
        d[number] = number*number
    return d


run(host='localhost', port=8080)
