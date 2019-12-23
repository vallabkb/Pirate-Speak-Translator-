#!/usr/bin/python3

'''
Program: simpleTalkServer.py
Modified by: Vallab Kunigal Badrish for CS 3470
Description: Prints what is received on a TCP socket.
'''

from socket import *
from sys import argv

PORTNUM =  65125
MAX_LINE = 4096

pirateSpeak = {"hello": "ahoy", "hi": "yo-ho-ho", "my": "me", "friend": "bucko", 
               "sir": "mate", "miss": "proud beauty", "stranger": "scurvy dog",
               "officer": "foul blaggart", "where": "whar", "is": "be", "the": 
               "thar", "you": "ye", "water": "rum", "nearby": "broadside", 
               "restroom": "head", "restaurant": "galley", "hotel":
               "fleabag inn"} # Dictionary to store all the pirate words#

if len(argv) == "-r":
   pirateSpeak = "r"

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('',PORTNUM))

serversocket.listen(5) #max 5 connections
	
while True:	
        connection, address = serversocket.accept()

        while True:
           try:
              buf = connection.recv(MAX_LINE)
              if len(buf) == 0: break
              print(buf.decode().strip())
           except KeyboardInterrupt:
              print("where de ye go?") #prints out the message enclosed in print when user closes server using ctr C#
           PirateTalk = buf.decode().split()
           pirateOutput = ""
           for i in PirateTalk:
              if i in pirateSpeak:
                 pirateOutput = pirateOutput + "" + pirateSpeak[i] # changing the normal words into piratespeak that is stored in the dictionary#
              else:
                 pirateOutput = pirateOutput + i
           connection.send(bytes(pirateOutput.encode()))# sending the modified string to client#
                
               



