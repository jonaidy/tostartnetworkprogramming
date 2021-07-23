import os

hostname = "192.168.1.100"

response = os.system("ping -c 2 " + hostname)
# In Unix, the return value is a 16-bit number that contains two different pieces of information. From the documentation

print(response)