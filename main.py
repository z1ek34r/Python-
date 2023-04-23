from flask import Flask, render_template, request, redirect,session
import getIp,nam1p,cms,subdomains,catalog,cdn,W21hois
import time
app = Flask(__name__)
app.secret_key='4c3b6dad1a5d9c2c958d13da998b9eee0f0c407d4cc360aa'
@app.route('/')
def index():
    return render_template('search.html')
@app.route('/search', methods=['GET','POST'])
def search():
    domain = request.form['domain']
    # print(domain)
    session['data'] = domain
    selected_color = request.form['type']
    print(selected_color)
    if selected_color == 'ip':
        return redirect('/getip')
    elif selected_color == 'nmap':
        return redirect('/namp')
    elif selected_color == 'cms':
        return redirect('/cms')
    elif selected_color == 'subdomain':
        return redirect('/subdomain')
    elif selected_color == 'catalog':
        return redirect('/catalog')
    elif selected_color == 'cdn':
        return redirect('/cdn')
    elif selected_color == 'whois':
        return redirect('/whois')
    elif selected_color == 'all':
        return redirect('/all')
    else:
        return '未完成'

@app.route('/getip')
def getip():
    domain = session.get('data',None)
    ip = getIp.get_ip(domain)
    return render_template('result.html',ip=ip,domain=domain+'的扫描结果')
@app.route('/namp')
def nmap():
    start_port = 1
    end_port = 1000
    domain = session.get('data',None)
    ip = getIp.get_ip(domain)
    results = nam1p.scan_ports(ip, start_port, end_port)
    return render_template('result.html',ports = results,domain=domain+'的扫描结果')

@app.route('/cms')
def c1ms():
    domain = session.get('data', None)
    httpurl = "http://"+session.get('data',None)
    session['httpurl'] = httpurl
    cmstype = cms.cms_detect(httpurl)
    return render_template('result.html',cms=cmstype,domain=domain+'的扫描结果')
@app.route('/subdomain')
def subdomain():
    domain = session.get('data',None)
    results = subdomains.scan_subdomains(domain)
    return render_template('result.html',subdomains=results,domain=domain+'的扫描结果')
@app.route('/catalog')
def cata1log():
    domain = session.get('data', None)
    httpip = "http://"+ domain
    results = catalog.scan_directory(httpip, 'dirs.txt', ['', '.html'], threads=20)
    return render_template('result.html',directories=results,domain=domain+'的扫描结果')

@app.route('/cdn')
def cd1n():
    domain = session.get('data', None)
    flag = cdn.detect_cdn(domain)
    if flag:
        return render_template('result.html',cdn='使用了CDN',domain=domain+'的扫描结果')
    else : return render_template('result.html',cdn='未检测到CDN',domain=domain+'的扫描结果')
@app.route('/whois')
def who1is():
    whoisdomain = session.get('data', None)
    if whoisdomain=='z1ek34r.com':
        whoisdomain = 'baidu.com'
    results = W21hois.whoiis(whoisdomain)
    results_list=[]
    results_list.append(results.registrar)
    results_list.append(results.emails[0])
    results_list.append(results.state)
    results_list.append(results.country)
    return render_template('result.html', whois_list=results_list, domain=whoisdomain + '的扫描结果')
@app.route('/all')
def all():
    domain = session.get('data', None)
    # 开始记录时间
    start_time = time.time()
    ip = getIp.get_ip(domain)
    start_port = 1
    end_port = 4000
    domain = session.get('data', None)
    nampresults = nam1p.scan_ports(ip, start_port, end_port)
    subresults = subdomains.scan_subdomains(domain)
    httpurl = "http://" + session.get('data', None)
    session['httpurl'] = httpurl
    cmstype = cms.cms_detect(httpurl)
    httpip = "http://" + domain
    catalogresults = catalog.scan_directory(httpip, 'dirs.txt', ['', '.html'], threads=20)
    whoisdomain = domain
    if whoisdomain == 'z1ek34r.com':
        whoisdomain = 'baidu.com'
    whoisresults = W21hois.whoiis(whoisdomain)
    whoisresults_list = []
    whoisresults_list.append(whoisresults.registrar)
    whoisresults_list.append(whoisresults.emails[0])
    whoisresults_list.append(whoisresults.state)
    whoisresults_list.append(whoisresults.country)
    flag = cdn.detect_cdn(domain)
    # 结束记录时间
    end_time = time.time()
    # 计算查询所用时间
    query_time = end_time - start_time
    # 将查询所用时间保存到本地txt文件中
    with open('query_time.txt', 'a') as f:
        f.write(f"查询域名 {domain} 所用时间：{query_time:.4f}秒\n")
    if flag:
        return render_template('result.html',ip=ip,cdn='使用了CDN',subdomains=subresults,directories=catalogresults,ports = nampresults,whois_list = whoisresults_list,cms=cmstype,domain=domain+'的扫描结果')
    else:return render_template('result.html',ip=ip,cdn='未检测到CDN',subdomains=subresults,directories=catalogresults,ports = nampresults,whois_list = whoisresults_list,cms=cmstype,domain=domain+'的扫描结果')
@app.errorhandler(Exception)
def handle_error(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug=True)
