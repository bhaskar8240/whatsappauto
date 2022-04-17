# import pywhatkit
from pythonping import ping
import datetime
import time
import re

# Regex create for Down and Up nodes.
Down_RE = r'Node down'
Up_RE = r'Node up'


#Open the Ip text file for Ping test.
with open("whatsappauto-main/ipaddress.txt") as f:
    device_ip = f.read().splitlines()
#Run the ping command through Module Pythoping (Where the Up and Down 
def ping_status(x):
    respon = ping(x, count=2, size=9)        
    if respon.packets_lost:
        return(f"{x} Node down")                
    else:
        return(f"{x} Node up")

def down_log_collect(output=None):
    for line in output.split("\n"):
        k = re.findall(Down_RE, line)    
        if k:
            data= open("whatsappauto-main/down_networkinfo.txt")
            for serach in data:
                if line in serach:
                    
                    break
            else:
                data= open("whatsappauto-main/down_networkinfo.txt","a")
                print(line,datetime.datetime.now(),file=data)
                

def up_log_collect(output=None):
    for line in output.split("\n"):
        k = re.findall(Up_RE, line)   
        if k:
            data= open("whatsappauto-main/networkinfo.txt")
            for serach in data:
                if line in serach:  
                    break
            else:
                data= open("whatsappauto-main/networkinfo.txt","a")
                print(line,datetime.datetime.now(),file=data)

def remove_if_not_up(output=None):
    down=  open("whatsappauto-main/networkinfo.txt","r+")
    down_data = down.readlines()
    for line in output.split("\n"):
        down.seek(0)
        for i in down_data:
            if not (line.startswith(line)):
                down.write(i)             
        down.truncate()


def remove_if_not_down(output=None):
    up= open("whatsappauto-main/down_networkinfo.txt","r+")
    up_data = up.readlines()
    for line in output.split("\n"):
        up.seek(0)
        for i in up_data:
            if not (line.startswith(line)):
                up.write(i)        
        up.truncate()

def down_host():
    with open ("whatsappauto-main\down_networkinfo.txt")as f:
        read = len(f.readlines())
        return  read
#Counting the Uphost        
def up_host():
    with open ("whatsappauto-main/networkinfo.txt")as f:
        read = len(f.readlines())
        return  read 
#Main function Run all the other function    
def main():
    while True:

        for ip in device_ip:
            ips=ip
            ping_start = ping_status(ips)
            if  "Node up" in ping_start:
                updata = ping_start
                up_log = up_log_collect(output=ping_start)         
            else:
                downdata = ping_start
                down_log = down_log_collect(output=ping_start)
        
            Down_node = down_host()
            Up_node = up_host()
        print("Up host:"+ str(Up_node))
        print("Down host:"+ str(Down_node))
        send_log_down = remove_if_not_up(output=downdata)
        send1_log_up = remove_if_not_down(output=updata)
        time.sleep(4) 



if __name__ == "__main__":
     main()


