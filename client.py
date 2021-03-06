import sys
from time import time

# add gen-py to PYTHONPATH
sys.path.append('./gen-py')

from hi import HelloWorld

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)

    transport.open()

    print "client - ping"
    print "server - " + client.ping()

    start_time = time()

    for x in xrange(0, 10):
        print "client Say: Hello!"
        msg = client.say("Hello!")
        print "server " + msg

    end_time = time() - start_time
    print "duration: " + str(end_time)
    transport.close()
except Thrift.TException, ex:
    print ex.message
