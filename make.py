#! usr/bin/python

open_file = input('Witch file will be the folder of enable_espion.batch file ?:')
close_file = input('Witch file will be the folder of disable_espion.batch file ?:')
d = {
	open_file+"/enable_espion.bat" : "netsh advfirewall firewall add rule name=\"Close Port 11300\" dir=in action=allow protocol=TCP localport=11300 remoteip=127.0.0.1" ,
	close_file+"/disable_espion.bat" : "netsh advfirewall firewall add rule name=\"Open Port 11300\" dir=in action=allow protocol=TCP localport=11300 remoteip=127.0.0.1",
}
for file, text in d.items():
	with open(file, 'w') as co: co.write(text)
