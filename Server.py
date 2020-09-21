#!/usr/bin/env python3


from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()


def get_users(app_id, username, password):
    if username != "joe" or password != "doe":
        print(401, 'Invalid username or password')
    else:
        return [{'Name': 'potato'}]


# while username == "joe" and password == "doe":
#    print[{'id': '1', 'Name': 'My Name'}]
# else:
#   print(401, 'Invalid username or password')


server.register_function(get_users, 'user.getUsers')

# Run the server's main loop
server.serve_forever()
