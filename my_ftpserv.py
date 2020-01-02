from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", r"D:\Niko\oneone", perm="elradfmwMT")
authorizer.add_user("user3", "incorrect", r"D:\Niko\oneone", perm="elradfmwMT")

#authorizer.add_anonymous("/home/nobody")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
