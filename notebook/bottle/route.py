from bottle import route, run
 
# http://localhost:8080/tags/abc
@route('/tags/<arg:re:[a-z]+>')
def tags(arg):
    return arg
 
# http://localhost:8080/num/123
@route('/num/<arg:int>')
def hello(arg):
    return str(arg)
 
run(host='localhost', port=8080)
