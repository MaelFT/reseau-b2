import psutil

def get_ip():
    print(psutil.net_if_addrs()['Wi-Fi'][1][1])

get_ip()