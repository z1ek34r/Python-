import threading
import queue
import socket

def scan_subdomains(domain):
    subdomains = [
        "www", "mail", "blog", "bbs", "chat", "shop", "web", "dev", "test", "m",
        "mobile", "mobi", "wap", "news", "mail", "pop", "smtp", "ftp", "dns", "ssl",
        "vpn", "gateway", "proxy", "cdn", "static", "img", "image", "cdn",
        "cache", "api", "admin", "mysql", "oracle", "svn", "git", "redis",
        "mongodb", "memcached", "ssh", "telnet", "imap", "smtp", "pop3", "pop",
        "imap4", "irc", "ldap", "radius", "sip", "xmpp", "vnc", "whois", "www1",
        "www2", "www3", "www4", "beta", "stage", "demo", "dev1", "dev2", "test1",
        "test2", "uat", "prod", "youxi","pikachu"
    ] # 假设要扫描的子域名列表
    results = [] # 用于保存扫描结果的列表

    # 将要扫描的子域名添加到队列中
    q = queue.Queue()
    for subdomain in subdomains:
        q.put(subdomain + '.' + domain)

    # 定义一个函数，用于检查子域名是否存在
    def check_subdomain():
        while True:
            try:
                subdomain = q.get_nowait()
            except queue.Empty:
                break

            try:
                ip = socket.gethostbyname(subdomain)
                results.append((subdomain, ip))
            except socket.error:
                pass

    # 创建多个线程并启动它们
    threads = []
    for i in range(10): # 假设使用10个线程进行扫描
        thread = threading.Thread(target=check_subdomain)
        thread.start()
        threads.append(thread)

    # 等待所有线程结束
    for thread in threads:
        thread.join()

    # 返回扫描结果
    return results
