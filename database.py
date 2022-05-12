import mariadb 
import sys
from openpyxl import load_workbook
import datetime


def all_nas():
    try:
       
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")

    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)     
    
    cur = connection.cursor()
    data = load_workbook("Nas_wise_location1.xlsx")
    data1 = data.active
    sr = data1["A"]
    Location = data1["B"]
    Ip = data1["C"]
    Status = data1["D"]
    Remarks = data1["E"]
    for s,l,i,st,r in zip(sr,Location,Ip,Status,Remarks):
        data1 = s.value
        data2 = l.value
        data3 = i.value
        # data4 = st.value
        # data5 = r.value
        try:
            time = datetime.datetime.now()
            formatted_date = time.strftime('%Y-%m-%d %H:%M:%S') 
            change = (f"UPDATE device SET Create = '{formatted_date}' WHERE Ip = '{data3}' ")
            # cur.execute("INSERT INTO device (Sr,Location,Ip,Create) VALUES (?, ?, ?, ?", (data1,data2,data3,formatted_date))
            cur.execute(change)
            print("Data execute") 
        except mariadb.Error as e: 
            print(f"Error: {e}")
    connection.commit()
    connection.close()

def down_log(down):
    time = datetime.datetime.now()
    formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(formatted_date)

    try:
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")
        cur = connection.cursor()
        cur.execute("INSERT INTO down_log (Location,Ip,Time) VALUES (?, ?, ?)", (" ",down,formatted_date))
        # print("Down Data execute")
        connection.commit()
        connection.close()
    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)     

def up_log(up):
    time = datetime.datetime.now()
    formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(formatted_date)
    try:
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")
        cur = connection.cursor()
        cur.execute("INSERT INTO up_log (Location,Ip,Time) VALUES (?, ?, ?)", (" ", up , formatted_date))
        # print("UP Data execute")
        connection.commit()
        connection.close()

    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)     

def temp_up_log(up):
    time = datetime.datetime.now()
    formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(formatted_date)
    try:
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")
        cur = connection.cursor()
        cur.execute("INSERT INTO temp_up (Ip,Datetime) VALUES (?, ?)", (up , formatted_date))
        # print("UP Data execute")
        connection.commit()
        connection.close()

    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)  

def temp_down_log(down):
    time = datetime.datetime.now()
    formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(formatted_date)
    try:
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")
        cur = connection.cursor()
        cur.execute("INSERT INTO temp_down (Ip,Datetime) VALUES (?, ?)", (down, formatted_date))
        # print("UP Data execute")
        connection.commit()
        connection.close()

    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)



def current_status(current,Ip):
    try:
        time = datetime.datetime.now()
        formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
        connection = mariadb.connect(
        user="root",
        password="gtpl@123",
        port=3306,
        database="device")
        cur = connection.cursor()
        change = (f"UPDATE device SET Status = '{current}' WHERE Ip = '{Ip}' ")
        change1 = (f"UPDATE device SET Uptime = '{formatted_date}' WHERE Ip = '{Ip}' ")
        cur.execute(change)
        cur.execute(change1)
        connection.commit()
        connection.close()
        print(cur.rowcount, "record(s) affected") 
    except mariadb.Error as e:
        print(f"Error connteting:{e}")   
        sys.exit(1)  

 


        

    
# def main():
#     all_nas()

# if __name__ == "__main__":
#      main()
   

