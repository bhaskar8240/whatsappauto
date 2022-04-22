# Import the module 
from pythonping import ping
import pywhatkit
import datetime
import time
import re

#create re for better match
Down_RE = r'Node down'
Up_RE = r'Node up'

#Open the ip list of the host.
with open("ipaddress1.txt") as f:
    device_ip = f.read().splitlines()

#Run the ping test. 
def ping_status(x):
    respon = ping(x, count=5, size=32)        
    if respon.packets_lost >= 1.0:
        return(f"{x} Node down")                
    else:
        return(f"{x} Node up")
#Down host log collect.(No Duplicate entry)
def down_log_collect(output=None):
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
#Up host log entry collect.(No duplicte entry)
def up_log_collect(output=None):
    for line in output.split("\n"):
        k = re.findall(Up_RE, line)   
        if k:
            data= open("networkinfo.txt")
            for serach in data:
                if line in serach:
                    
                    break
            else:
                data= open("networkinfo.txt","a")
                print(line,datetime.datetime.now(),file=data)
#If host not up from Up host log Send in whats app group and remove from up list.
def remove_if_not_up(output=None):
   
    down=  open("networkinfo.txt","r")
    down_data = down.readlines()
    change=  open("networkinfo.txt","w")
    for line in down_data:
        if line.find(output) != -1:
            sms= output + "Host is down"
            pywhatkit.sendwhatmsg_to_group_instantly(f"Lmj4HDmcvkk91oAXSKMoXx",{sms},20,tab_close=True)
            pass
        else:
            change.write(line)
            
#If host up from Down host log send in whats app group and remove from down list.
def remove_if_not_down(output=None):
    up= open("down_networkinfo.txt","r")
    up_data = up.readlines()
    change= open("down_networkinfo.txt","w")
    for line in up_data:
        if line.find(output) != -1:
            sms= output + "Host is Up"
            pywhatkit.sendwhatmsg_to_group_instantly(f"Lmj4HDmcvkk91oAXSKMoXx",{sms},20,tab_close=True)
            pass
        else:
            change.write(line)
#Count the Down host.
def down_host():
    with open ("down_networkinfo.txt")as f:
        read = len(f.readlines())
        return  read
#Count the Uphost.        
def up_host():
    with open ("networkinfo.txt")as f:
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
                up_ip_info = updata.replace("Node up","")
                up_log = up_log_collect(output=ping_start)
                send1_log_up = remove_if_not_down(output=up_ip_info)                 
            else:
                downdata = ping_start  
                ip_info = downdata.replace("Node down","")
                down_log = down_log_collect(output=ping_start)
                send_log_down = remove_if_not_up(output=ip_info)

        Down_node = down_host()
        Up_node = up_host()
        print("Up host:"+ str(Up_node))
        print("Down host:"+ str(Down_node))

        time.sleep(4) 

if __name__ == "__main__":
     main()

