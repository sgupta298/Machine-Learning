#!/usr/bin/python3
from scapy.all import *
ls()
b=ICMP()
b.show()
a=IP()
a.show()
a.dst = "192.168.1.130"
send(a/b)
a.src="www.google.com"
send(a/b)