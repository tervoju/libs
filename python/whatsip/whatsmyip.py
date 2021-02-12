import sys

# public IP
# required for port forwarding

from urllib.request import urlopen

with urlopen('http://icanhazip.com/') as url:
    s = url.read()

print(s.decode("utf-8").strip('\n'))