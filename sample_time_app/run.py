from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    import time
    return time.strftime('%H:%M:%S', time.localtime())


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
