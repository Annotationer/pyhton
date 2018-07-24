#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import socket
import multiprocessing

def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    print("request-data:" ,request_data)
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: my server\r\n"
    response_body = "hello python\r\n"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response:",response)
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #host = socket.gethostname()
    #print(host)
    server_socket.bind(("", 8000))
    server_socket.listen()
    
    while True:
        client_socket,client_address = server_socket.accept()
        handle_client_process = multiprocessing.Process(target = handle_client, args = (client_socket,) )
        handle_client_process.start()
        client_socket.close()

