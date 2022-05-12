# Import the module 
from pythonping import ping
import time
import re
import database


#create re for better match
Down_RE = r'Node down'
Up_RE = r'Node up'

#Open the ip list of the host.
# with open("ipaddress.txt") as f:
#     device_ip = f.read().splitlines()

#Run the ping test. 
def ping_status(x):
    respon = ping(x, count=5, size=9)  
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
                print(line,file=data)
                database.temp_down_log(line)
                
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
                print(line,file=data)
                database.temp_up_log(line)
                
#If host not up from Up host log Send in whats app group and remove from up list.
def remove_if_not_up(output=None):
    down=  open("networkinfo.txt","r")
    down_data = down.readlines()
    change=  open("networkinfo.txt","w")
    for line in down_data:
        if line.find(output) != -1:
            sms= output + "Host is Down" 
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
        with open("ipaddress.txt") as f:
            device_ip = f.read().splitlines()
        for ip in device_ip:
            ips=ip
            ping_start = ping_status(ips)
            if  "Node up" in ping_start:
                updata = ping_start
                # ms = (respon.rtt_avg_ms) 
                up_ip_info = updata.replace("Node up","")
                database.up_log(up_ip_info)
                database.current_status("up",up_ip_info)
                up_log = up_log_collect(output=ping_start)
                send1_log_up = remove_if_not_down(output=up_ip_info)                 
            else:
                downdata = ping_start  
                ip_info = downdata.replace("Node down","")
                database.down_log(ip_info)
                database.current_status("down",ip_info)
                down_log = down_log_collect(output=ping_start)
                send_log_down = remove_if_not_up(output=ip_info)

        Down_node = down_host()
        Up_node = up_host()
        print("Up Nas:"+ str(Up_node))
        print("Down Nas:"+ str(Down_node))

        time.sleep(4) 

if __name__ == "__main__":
     main()

