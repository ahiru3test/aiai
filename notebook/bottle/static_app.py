import os
from bottle import route, run, static_file

print((os.path.dirname(__file__) + "\\static").replace("\\","/"))

@route('/static/<filename>')
def server_static(filename):
    print(filename)
    # return static_file(filename, root='C:/Users/ai/notebooks/bottle/static')
    # filename = os.path.abspath(".") + "\\static" # For VScode
    # filename = (os.path.abspath(__file__) + "\\static").replace("\\","/")
    filepath = (os.path.dirname(__file__) + "\\static").replace("\\","/")
    return static_file(filename, root=filepath)
 
run(host='localhost', port=8080)
 
#http://localhost:8080/static/index.html
