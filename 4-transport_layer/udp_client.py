import socket

def run_udp_client():
    #initialize UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Sending datagrams
    while (1):
        message = input("Enter the datagram (or 'exit' for exit) ")
        if message.lower() == 'exit':
            break
        client_socket.sendto(message.encode(), ('localhost', 5003))

        #Receive answer from server
        data, addr = client_socket.recvfrom(1024)
        print("Server reply: ", data.decode())

    #end of connetion
    client_socket.close()

run_udp_client()