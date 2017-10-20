 print '\n\n',sockets
            if not message:
                print "Client disconnected."
                addIndex=sockets.index(self._client)
                del sockets[addIndex]
                del addresses[addIndex]
                self._client.close()
                break
            else:
                if 'ONLINE#' in message:
                    for x in sockets:
                        if (x!=self._client):
                            try:
                                x.send(message[7:])
                            except:
                                print 'disconnected'
                                continue
                    print message[7:]
                else:     
                    for x in sockets:
                        try:
                            x.send(message)
                            #/*sockets is the list of all client*/
                        except:
                            print ' '
                            continue
                    print message