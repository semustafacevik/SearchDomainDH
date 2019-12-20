from Extensions.functions import *
import socket
import threading

class PortScanSearch:

    def __init__(self, word):

        self.threads = 25
        self.host = word
        self.ports = [21, 22, 80, 443, 8080]
        self.lock = threading.BoundedSemaphore(value=self.threads)
        self.openports = ''

    def do_search_portscan(self):

        print('\nSearching PortScan...')
        self.lock.acquire()
        for port in self.ports:
            try:
                connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connect.settimeout(2)
                p_result = connect.connect_ex((self.host, int(port)))
                if p_result == 0:
                    self.openports += str(port) + " * "
                connect.close()

            except Exception as e:
                print(e)

        self.lock.release()

        if(len(self.ports)) == 0:
            print("No ports found on host: {0}".format(host))

        result['result_portscanner'] = self.openports
        print('OK - PortScanner!')