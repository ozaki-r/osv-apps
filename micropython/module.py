from osv.modules import api

default = api.run("/tools/micropython.so /tools/sock-server.py")
