from pip import main
from pythonping import ping

with open ("E:\Python code\log.txt","r")as f:
    data = f.read().split(",")

with open('E:\Python code\sacn\ip.txt') as f:
        host_addrs = f.read().splitlines()
 
while True:

    def auto():
        print("""
        +-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+
        |f|a|s|t| |p|i|n|g| |s|e|r|v|e|r|
        +-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+
        """)
        for ip in host_addrs:
            res = ping(ip,count=1)
            if  res.packet_loss == 1.0:
                print(ip , end=" ")
                print("Node is down",end=" ")
                print(res.packet_loss)            
            else:
                print(ip , end=" ")
                print("Node is up",end=" ")
                print(res.rtt_avg_ms,end=" ")
                print(res.packet_loss)
    if __name__ == "__main__":
        main()
                   
