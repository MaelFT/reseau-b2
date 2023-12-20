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
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
        for line in lines:
            print(line)
            r = get_content(line)
            print(r)
            write_content(r.content, line[8:-2])
        stop = time.perf_counter()
        print('Done in {} seconds'.format(stop - start))
