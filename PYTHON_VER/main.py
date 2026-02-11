from bottle import route, run, template

@route('/GetMessages/<id>')
def index(id):
    return {
        "id": id,
        "messages": [
            
        ]
    }

run(host='127.0.0.1', port=8080)