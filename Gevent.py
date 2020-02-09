
#from gevent.wsgi import WSGIServer
from gevent.pywsgi import WSGIServer
from main import app

http_server = WSGIServer(('192.168.1.18', 80), app)
http_server.serve_forever()
print("1")

