from wsgiref.simple_server import make_server
from thesaurus.wsgi import application


if __name__ == '__main__':
    server = make_server('0.0.0.0', 6543, application)
    print('ready')
    server.serve_forever()
