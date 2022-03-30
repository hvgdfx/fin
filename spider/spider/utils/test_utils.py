import socket

local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)

if local_ip == "120.132.33.146":
    is_test_enviroment = True
else:
    is_test_enviroment = False
