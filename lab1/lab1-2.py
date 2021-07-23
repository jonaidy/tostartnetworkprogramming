import os

hostname = "www.google.com"
response = os.system("ping -c 2 " + hostname)

'''In Unix/Linux, the return value is a 16-bit number that contains two different pieces of information.
From the documentation "a 16-bit number, whose low byte is the signal number that killed the process,
and whose high byte is the exit status (if the signal number is zero)'''

if response == 0:
    pingstatus = "Reachable"
else:
    pingstatus = "Unreachable"

print(hostname + ' is ' + pingstatus)




