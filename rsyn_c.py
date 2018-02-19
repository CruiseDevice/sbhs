import subprocess,os,sys
#from settings import BASE_DIR
def rsyn_c():
	#ipaddrs_list = os.path.join(BASE_DIR,"RPi_data")
	ip_list = []
	with open('/home/vlabs-sbhs/code/sbhs/sbhs_server/RPi_data/ipaddrs.txt','r') as f:
		for line in f:
			ip_list.append(line.strip().split('\n'))
        print ip_list
	for ip in ip_list:
                print ip
		ip = "".join(str(i) for i in ip)
		source = "pi@"+ip+":/home/pi/sbhs-pi/experiments/"
		bashCommand = [
           		"rsync",
				"-av",
           		"-arz",
            		"--remove-source-files",
            		"-e",
            		"ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
            		"--progress",
            		source,
			"/home/vlabs-sbhs/code/sbhs/experiments/"
        	]
		print bashCommand
		subprocess.call(bashCommand)
rsyn_c()
