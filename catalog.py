import requests
from concurrent.futures import ThreadPoolExecutor


def scan_directory(url, directories_file, extensions, threads=10):
    results = []
    with open(directories_file, 'r') as f:
        directories = f.read().splitlines()

    def check_dir(directory):
        if not directory.startswith('/'):
            directory = '/' + directory
        for extension in extensions:
            path = url + directory + extension
            response = requests.get(path)
            if response.status_code == 200:
                results.append(path)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for directory in directories:
            executor.submit(check_dir, directory)

    return results


if __name__ == '__main__':
    results = scan_directory('http://z1ek34r.com', 'dirs.txt', ['', '.html'], threads=20)
    str=''
    for result in results:
        str += result+"\n"
    print(str)
