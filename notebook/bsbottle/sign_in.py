from bottle import route, run, static_file, post, template, request
import os

basedir = os.path.dirname(os.path.abspath(__file__))

@route('/sign-in/<filepath:path>')
def index(filepath):
    # index.html, sign-in.css のGET処理
    print(filepath)
    # return static_file(filepath, root='C:/Users/ai/notebooks/bsbottle/sign-in/')
    return static_file(filepath, root= basedir + '/sign-in/')

@route('/assets/<filepath:path>')
def assets(filepath):
    # cs, js のGET処理
    print("assets:",filepath)
    # return static_file(filepath, root='C:/Users/ai/notebooks/bsbottle/assets/')
    return static_file(filepath, root= basedir + '/assets/')

@post('/sign-in/sign-in') 
def sign_in():
    # フォームからPOSTされたデータを取得する
    username = request.forms.decode().get('username')
    password = request.forms.decode().get('password')
    if password == "pingpong":
        return template("<p>Your login information was correct. welcome {{username}}</p>", username=username)
    else:
        return "<p>Login failed.</p>"
 
run(host='localhost', port=8080)
 
#http://localhost:8080/sign-in/index.html