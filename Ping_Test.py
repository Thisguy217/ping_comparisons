from pythonping import ping
import matplotlib.pyplot as plt
import numpy as np
import time
import csv

#Timer for pings start
start_time=time.time()

#data input
cloudflare=ping('1.1.1.1', size=64, count=1000, timeout=10)
google=ping('8.8.8.8', size=64, count=1000, timeout=10)
opendns=ping('208.67.222.222', size=64, count=1000, timeout=10)

print("---%s seconds ---" % (time.time() - start_time))

data= {'Cloudflare':cloudflare.rtt_avg_ms,'Google':google.rtt_avg_ms,'OpenDNS':opendns.rtt_avg_ms}
IP= list(data.keys())
ms = list(data.values())

fig = plt.figure(figsize = (10,5))

#graphical output
plt.bar(IP, ms, color = 'maroon', width = 0.4)

plt.xlabel("IP Addresses")
plt.ylabel("Millisecond response time")
plt.title("Ping Test for DNS response")
plt.savefig('Ping Test for DNS response.png', dpi=400)
plt.show()

#csv output
with open('Data.csv', 'w', newline='') as csvfile:
    fieldnames= ['Cloudflare','Google','OpenDNS']
    thewriter =csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    for ms in ms:
        thewriter.writerow(data)