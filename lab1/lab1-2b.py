import subprocess
from datetime import datetime
#hostname = "192.168.1.100"
#wide = 10
hostnames = ["192.168.1.100", "www.youtube.com", "www.ncs.co"]
#hostnames = []
results = {}
for hostname in hostnames:
    try:
        response = subprocess.check_output(
            ['ping', '-c', '3', hostname],
            stderr=subprocess.STDOUT, # get all output
            universal_newlines=True # return string not bytes
        )
        pingtest = 'Reachable.'
        results[hostname] = pingtest
        #print(f'{hostname} is {pingtest}.')
    except subprocess.CalledProcessError:
        response = None
        pingtest = 'Unreachable.'
        #print(f'{hostname} is {pingtest}')
        results[hostname] = pingtest

now = datetime.now()
nowstring = now.strftime("%d/%m/%Y %H:%M:%S")

with open("result.txt","a") as resulttext:
    for key, value in results.items():
        # print(f'{key} is {value}')
        resultstrg = f'{key} is {value} at {nowstring}\n'
        resulttext.writelines(resultstrg)

