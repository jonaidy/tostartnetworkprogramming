import subprocess

hostname = "www.google.com"
try:
    response = subprocess.check_output(
        ['ping', '-c', '3', hostname],
        stderr=subprocess.STDOUT, # get all output
        universal_newlines=True # return string not bytes
    )
except subprocess.CalledProcessError:
    response = None

print(response)
