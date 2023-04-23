import socket
import requests

def get_ip_from_dns(domain):
    """
    通过域名获取IP地址
    """
    return socket.gethostbyname(domain)

def get_ip_from_http(url):
    """
    通过HTTP请求获取IP地址
    """
    try:
        r = requests.get(url, timeout=5)
        return r.json()['origin']
    except:
        return None

def detect_cdn(domain):
    """
    判断一个域名是否使用CDN
    """
    dns_ip = get_ip_from_dns(domain)
    http_ip = get_ip_from_http('http://' + domain)
    if dns_ip and http_ip and dns_ip != http_ip:
        return True
    else:
        return False
if __name__ == '__main__':
    url=input("输入URL：")
    flag = detect_cdn(url)
    if flag :
        print("使用了CDN.")
    else:
        print("没有使用CDN")