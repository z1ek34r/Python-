import whois
def whoiis(domain):
    w = whois.whois(domain)
    return w
if __name__ == '__main__':
    domain_name = input("请输入您要查询的域名：")
    w = whoiis(domain_name)
    print(w)
    print(w.registrar)
    print(w.emails[0])
    print(w.state)
    print(w.country)
