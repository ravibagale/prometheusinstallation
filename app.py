import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter,generate_latest, CONTENT_TYPE_LATEST
from flask import Flask

app = Flask(__name__)
REQUESTS = Counter('hello_worlds_total','Hello Worlds requested.')
@app.route('/')
def hello_world():
    REQUESTS.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    # Run the Flask app and listen on all network interfaces
     #start_http_server(8000)
     app.run(host='0.0.0.0', debug=True)
