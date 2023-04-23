"""
author:张军杰
学号：201911010322
班级：网安本1901
"""
import socket
def get_ip(url):
    ip = socket.gethostbyname(url)
    print(url,"的IP地址是:", ip)
    return ip
if __name__ == '__main__':
    get_ip("z1ek34r.com")