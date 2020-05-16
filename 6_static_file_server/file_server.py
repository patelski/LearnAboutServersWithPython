from bottle import route, run, static_file


@route('/img/<picture>')
def serve_pictures(picture):
    return static_file(picture, root='img')


run(host='localhost', port=8080)
