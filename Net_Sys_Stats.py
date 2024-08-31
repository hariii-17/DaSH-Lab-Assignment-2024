#SYSTEM STATS


import psutil #processing system utilities
#CPU Percent
#print(psutil.cpu_percent(2)) #Argument given is the time interval. Calculated the CPU utilized in the form of percentage in the given time interval.

#Disk Usage
d_use=psutil.disk_usage("/")
#print("\nTotal = ",d_use.total//(2**30))
#print("Used = ",d_use.used//(2**30))
#print("Free = ",d_use.free//(2**30))


#NETWORK STATS

#Bandwidth Usage

bytes_recv = psutil.net_io_counters().bytes_recv
bytes_sent = psutil.net_io_counters().bytes_sent
total_bytes = bytes_recv + bytes_sent

#print("\nBytes Received = ",bytes_recv,"\nBytes Sent = ",bytes_sent,"\nTotal = ",total_bytes)

import speedtest
st=speedtest.Speedtest()
download_speed=st.download()/(1024*1024*8)
upload_speed=st.upload()/(1024*1024*8)
#print("Download speed = ",download_speed/(1024*1024*8),"MB")
#print("Upload speed = ",upload_speed/(1024*1024*8),"MB")

#Latency in milliseconds
servernames=[] #takes the closest major server as default
st.get_servers(servernames)
#print(st.results.ping)

import csv
f= open("stats.csv",'w')
writer=csv.writer(f)
writer.writerow(('CPU Utilized','Total Disk Space','Used Space in Disk','Free Space in Disk','Bytes Received','Bytes Sent','Total Bytes','Download Speed','Upload Speed','Latency'))
writer.writerow((psutil.cpu_percent(2),d_use.total//(2**30),d_use.used//(2**30),d_use.free//(2**30),bytes_recv,bytes_sent,total_bytes,download_speed,upload_speed,st.results.ping))