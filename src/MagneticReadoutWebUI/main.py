from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# UGLY IMPORT FROM PARENT DIRECTORY
import sys
sys.path.append('../MagneticReadoutProcessing')
from MagneticReadoutProcessing import MRPReading
#from MRPProject.MagneticReadoutProcessing import MRPReading


def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()