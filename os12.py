import requests

url = "http://z1ek34r.com"
response = requests.get(url)

server_header = response.headers.get('Server')
if server_header:
    if 'windows' in server_header.lower():
        print('The server is running on a Windows OS')
    elif 'linux' in server_header.lower():
        print('The server is running on a Linux OS')
    elif 'mac' in server_header.lower():
        print('The server is running on a Mac OS')
    else:
        print('The server OS is unknown')
else:
    print('Server header not found')
