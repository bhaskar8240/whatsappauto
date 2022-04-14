# import pywhatkit
from pythonping import ping
import datetime
import time
import re
import pandas as pd

Down_RE = r'Node down'
Up_RE = r'Node up'

with open("ipaddress.txt") as f:
    device_ip = f.read().splitlines()


def ping_status(x):
    respon = ping(x, count=2, size=9)        
    if respon.packets_lost:
        return(f"{x} Node down")                
    else:
        return(f"{x} Node up")

def log_collect(output=None):
    for line in output.split("\n"):
        k = re.findall(Down_RE, line)
        if k:
            data= open("down_networkinfo.txt")
            for serach in data:
                if line in serach:
                    break
            else:
                data= open("down_networkinfo.txt","a")
                print(line,datetime.datetime.now(),file=data)
        else:
            data= open("up_networkinfo.txt")
            for serach in data:
                if line in serach:
                    break
            else:
                data= open("up_networkinfo.txt","a")
                print(line,datetime.datetime.now(),file=data)
            


def down_host():
    with open ("down_networkinfo.txt")as f:
        read = len(f.readlines())
        return  read
def up_host():
    with open ("up_networkinfo.txt")as f:
        read = len(f.readlines())
        return  read   


def main():
    for ip in device_ip:
        ips=ip
        ping_start = ping_status(ips)
        log = log_collect(output=ping_start)
        Down_node = down_host()
    
        Up_node = up_host()
    print("Up host:"+ str(Up_node))
    print("Down host:"+ str(Down_node)) 
if __name__ == "__main__":
     main()

