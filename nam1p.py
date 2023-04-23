import socket
import threading

def scan_port(host, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host, port))
        results.append(port)
    except:
        pass
    sock.close()

def scan_ports(host, start_port, end_port):
    threads = []
    results = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port, results))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

if __name__ == '__main__':
    host = input("请输入要扫描的主机名或IP地址: ")
    start_port = int(input("请输入起始端口: "))
    end_port = int(input("请输入结束端口: "))
    results = scan_ports(host, start_port, end_port)
    str1 = ''
    for i in results:
        str1+=str(i)+" "
    print(str1)
