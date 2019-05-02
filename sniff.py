from scapy.all import *
import socket
import requests
import json

apiIP = "69.195.146.130"

def pkt_callback(pkt):

    if TCP in pkt:
        if pkt[IP].src != apiIP and pkt[IP].dst != apiIP:
            print(" -- Source IP: " + pkt[IP].src)

            try:
                srcHost = socket.gethostbyaddr(pkt[IP].dst)[0]
                print("    Source IP Belongs To: " + srcHost)
                #r = requests.get("http://ip-api.com/json/" + pkt[IP].src).json()
                #print(     "IP Src Is From: " + r['regionName'])
            except:
                a = 0
            print("    Destination IP: " + pkt[IP].dst)

            try:
                dstHost = socket.gethostbyaddr(pkt[IP].src)[0]
                print("    Destination IP Belongs To: " + dstHost)
                #r = requests.get("http://ip-api.com/json/" + pkt[IP].dst).json()
                #print(     "IP DSt Is From: " + r['regionName'])
            except:
                a = 0

            try:
                print("    data: " + pkt[Raw].load.decode('utf-8'))
            except:
                print("Not able to print data")
def main():
    a = sniff(lfilter = pkt_callback)

if __name__ == '__main__':
    main()
