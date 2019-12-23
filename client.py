#!/usr/bin/python3

'''
Program: simpleTalkClient.py
Modified by: Vallab Kunigal Badrish  for CS 3470
Description: Sends a string to a server over a TCP socket.
'''

from socket import *
from sys import argv

PORTNUM = 65125
MAX_LINE = 4096

rhost = "student.cs.uni.edu"

if len(argv) > 1:
	rhost = argv[1]

dest = gethostbyname(rhost)

addr=(dest, PORTNUM)                  
s = socket(AF_INET, SOCK_STREAM)
s.settimeout(1.5)  
s.connect(addr)  # connects to the server#


while True:

	try:
		buf = input("") #Takes in an input from the user#
	except EOFError:
		break;

	s.send(bytes(buf + "\n", 'ascii')) # sends the string inputted by the user to the server"
	buf = s.recv(MAX_LINE) #Recives the modified string sent from the server#
	if len(buf) == 0: break
	print(buf.decode().strip())
                
