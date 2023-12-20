import requests
import time
import sys

def get_content(url):
    return requests.get(url)

def write_content(content, file):
    with open('tmp/' + file, 'w') as f:
        f.write(str(content))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start = time.perf_counter()
        r = get_content(sys.argv[1])
        write_content(r.content, 'title.txt')
        stop = time.perf_counter()