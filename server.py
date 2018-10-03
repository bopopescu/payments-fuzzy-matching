import os

from bottle import route, run, static_file, get, request
from app import validate_payment

@route('/')
def server_static(filename = 'index.html'):
    return static_file(filename, root="static/")

@route('/api/v1', method=['GET'])
def apiv1():
    return validate_payment(request.query['name'], request.query['sort_code'], request.query['account_number'], 70)

# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=3000, debug=True)