from scapy.all import sniff, IP, IPv6, ICMP

#Function for handling captured package
def packet_handler(packet):
    #check IP layer is availaible
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print("\n=====IPv4 packet=====")
        print('-' * 40)
        print(f"| {'Version: ':<30} | {ip_layer.version} (IPv4) ")
        print(f"| {'Длина заголовка: ':<30} | {ip_layer.ihl * 4} байт ")
        print(f"| {'Тип обслуживания: ':<30} | {ip_layer.tos} ")
        print(f"| {'Packet lenght: ':<30} | {len(packet)} байт ")
        print(f"| {'Identification ':<30} | {ip_layer.id} ")
        print(f"| {'Flags: ':<30} | {ip_layer.flags} ")
        print(f"| {'Смещение фрагмента: ':<30} | {ip_layer.frag} ")
        print(f"| {'TTL : ':<30} | {ip_layer.ttl} ")
        print(f"| {'Protocol: ':<30} | {ip_layer.proto} (0x{ip_layer.proto:X})")
        print(f"| {'Checksum: ':<30} | {ip_layer.chksum} ")
        print(f"| {'Source IPv4: ':<30} | {ip_layer.src} ")
        print(f"| {'Destination IPv4: ':<30} | {ip_layer.dst} ")
    
    elif packet.haslayer(IPv6):
        ipv6_layer = packet[IPv6]
        print("\n=====IPv6 packet=====")
        print('-' * 40)
        print(f"| {'Version: ':<30} | {ipv6_layer.version} (IPv6) ")
        print(f"| {'Traffic class: ':<30} | {ipv6_layer.tc} ")
        print(f"| {'Flow label: ':<30} | {ipv6_layer.fl} ")
        print(f"| {'Payload lenght : ':<30} | {len(ipv6_layer.payload)} байт ")
        print(f"| {'Next title: ':<30} | {ipv6_layer.nd} (0x{ipv6_layer.nh:X})")
        print(f"| {'TTL : ':<30} | {ipv6_layer.hlim} ")
        print(f"| {'Source IPv6: ':<30} | {ipv6_layer.src} ")
        print(f"| {'Destination IPv6: ':<30} | {ipv6_layer.dst} ")
        print('-' * 40)
        
#start sniff
print("Start sniffing package...")
sniff(prn = packet_handler, count = 2) #sniff 2 frames