import os
hostname = "shootforthegoal.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is up!')