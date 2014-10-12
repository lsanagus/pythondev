import random
from random import randint

import string
from twisted.internet import protocol, reactor

class EchoClient(protocol.Protocol):
    def connectionMade(self):
	rand_name = ''.join(random.sample(string.hexdigits, 8))
	rand_number1 = str( randint(100,900) )
	rand_number2 = str( randint(10,99) )
	rand_number3 = str( randint(1000,9999) )
        self.transport.write("Name: {0} Social#: {1}-{2}-{3}".format(rand_name.upper(), rand_number1, rand_number2, rand_number3 ) )

    def dataReceived(self, data):
	print "Server received: ", data
        self.transport.loseConnection()
        
class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed."
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "connection lost."
        reactor.stop()
    
reactor.connectTCP("localhost",8000,EchoFactory())
reactor.run()
            
