#!/uimport socket
import sys

sys.path.append('./gen-py')

from hi import HelloWorld
from hi.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloWorldHandler:
    def __init__(self):
        pass

    @staticmethod
    def ping():
        return "pong"

    @staticmethod
    def say(msg):
        ret = "Received: " + msg
        print ret
        return ret


handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting thrift server in python..."
server.serve()
print "done!"
