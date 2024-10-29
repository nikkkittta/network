from scapy.all import sniff, Ether

def frame_handler(frame):
    #проверяем наличие Ethernet frame
    if frame.haslayer(Ether):
        ethernet_layer = frame[Ether]

        #получаем поля Ethernet frame
        src_mac =   ethernet_layer.src
        dst_mac =   ethernet_layer.dst
        eth_type =  ethernet_layer.type
        payload =   ethernet_layer.payload

        crc = b'\x00\x00\x00\x00'               #пример контрольной суммы 


        # Форматируем вывод Ethernet frame(a) в виде таблицы
        print("\n ====Ethernet Frame====")
        print("-" * 40)
        print(f"| {'Source MAC adreess: '     : <30} | {src_mac}  (6 bytes)  |")
        print(f"| {'Destination MAC adreess: ' :<30} | {dst_mac}  (6 bytes)  |")
        print(f"| {'Protocol type: '           :<30} | {eth_type} (0x{eth_type:X})    (2 bytes) |")
        print(f"| {'Data field: '              :<30} | {bytes(payload)}  {len(payload)}   bytes  |")
        print(f"| {'Checksum (CRC): '          :<30} | {crc}  (4 bytes)  |")
        print(f"| {'Ethernet header size: '    :<30} | {len(ethernet_layer)}  bytes  |")    
        print("-" * 40)


#Start sniff frames
print("Start sniff Ethernet frames.....\n")
sniff(prn=frame_handler, count = 2)