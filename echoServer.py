#!/usr/bin/env python3

#Phyton Servoer Echo Programm

# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces // alle vorhandenen ip-adressen
PORT = 8000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #wird s zugeordnet
    s.bind((HOST, PORT))    #Bindet HOST und PORT //"Adresse mit mehreren Türen"
    s.listen(1)   # hört ob daten kommen
    while True:   # client loop
        conn, addr = s.accept() #conn wird socket von client und addr die IP Adresse von client
        with conn:
            print('Connected by', addr)
            count=0
            while True:
                count=count+1
                print(count)
                data = conn.recv(16)  #Daten vom Client werden empfangen (zahl) gibt die menge der bytes an
                #receved from client            
                if not data: break      #Wenn keine Daten dann bricht er ab
                outdata = data[::-1]    #revers string /dreh die daten um hallo -> ollah
                print(outdata)
                conn.sendall(outdata)   #conn.sendall(data) -> conn.sendall(outdata)   alles wird geschickt
                                        #bis der Inhalt plus alle paketdaten gesendet sind. die Paketgrösse ist
                                    #genormt. ist ein paket größer, wird
