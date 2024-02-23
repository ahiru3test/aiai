from bottle import route, run, template
import datetime

@route('/')
def index():
    t = datetime.datetime.now()
    
    return template("""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="refresh" content="2; URL=">
    <title>Document</title>
<b>現在時刻 <br>{{t}}</b>""", t=t)

run(host='localhost', port=8080, reload=True, debug=True)
