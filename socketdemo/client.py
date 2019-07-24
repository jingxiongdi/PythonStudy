import socket
ip_port = ('169.254.198.157',9999)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.connect(ip_port)
while True:
    inp = input('数据：').strip()
    if inp == 'exit':
        break
    sk.sendto(bytes(inp,encoding='utf8'),ip_port)

sk.close()