import socket

def start_udp_server():
    #initialize UDP-socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5003))
    print("UDP server starts. Waiting datagrams...")

    #getting and handling datagrams
    while (1):
        data, addr = server_socket.recvfrom(1024)
        datagram = data.decode()
        print(f"Received datagram from {addr} : {datagram}")
        response = f"Datagram '{datagram}' received"
        server_socket.sendto(response.encode(), addr)

start_udp_server()