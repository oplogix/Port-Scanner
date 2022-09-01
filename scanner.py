#!/bin/python3

import socket

from datetime import datetime



#Define our target

if len(sys.argv) == 2:

	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

else:

	print("Invalid ammount of arguements.")

	print("Syntax: python3 scanner.py <ip>")

	

# Add a pretty banner



print(print("""



░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

    ███████              ████                     ███             

  ███░░░░░███           ░░███                    ░░░              

 ███     ░░███ ████████  ░███   ██████   ███████ ████  █████ █████

░███      ░███░░███░░███ ░███  ███░░███ ███░░███░░███ ░░███ ░░███ 

░███      ░███ ░███ ░███ ░███ ░███ ░███░███ ░███ ░███  ░░░█████░  

░░███     ███  ░███ ░███ ░███ ░███ ░███░███ ░███ ░███   ███░░░███ 

 ░░░███████░   ░███████  █████░░██████ ░░███████ █████ █████ █████ 𝟚𝟘𝟚𝟚

   ░░░░░░░     ░███░░░  ░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░░ ░░░░░ 

               ░███                     ███ ░███                  

               █████                   ░░██████                   

              ░░░░░                     ░░░░░░                    

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄▄░▄▄

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

  ___ 

 |\__\   - Port Scanner

 \|__|   - Made through TCM Security PEH Course

 

"""))

print("\n")

print("-" * 50)

print("Scanning Target "+target)

print("Time Started: "+str(datetime.now()))

print("-" * 50)



try:

	for port in range(50,85):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port)) #returns an error indicator

		if result == 0:

			print("Port {} is open".format(port))

		s.close()

except KeyboardInterrupt: #ctrl + c

	print("\nExiting Program.")

	sys.exit()

except socket.gaierror:  # cannot resolve hostname

	print("Hostname could not be resolved.")

except socket.error:   #error with socket

	print("Couldn't connect to server.")

	sys.exit()







