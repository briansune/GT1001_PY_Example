#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '192.168.0.1'
PORT = 60000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(10)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    print(connection, client_address)

    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data)
            if data:
                connection.sendall(data)
            else:
                break

    finally:
        # Clean up the connection
        connection.close()
