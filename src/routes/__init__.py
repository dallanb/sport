from .. import api
from .v1 import PingAPI
from .v1 import SportsAPI, SportsListAPI

# Ping
api.add_resource(PingAPI, '/ping', methods=['GET'])

# Sports
api.add_resource(SportsAPI, '/sports/<uuid:uuid>', endpoint="sport")
api.add_resource(SportsListAPI, '/sports', endpoint="sports")
