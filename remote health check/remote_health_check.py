import paramiko
import json
import os
from datetime import datetime

#configuration
HOST = "host_name"
USERNAME = "username"
KEY_FILE = "path/to/key"
COMMANDS = {
    "uptime": "uptime",
    "cpu": "top -bn1 | grep 'Cpu(s)'",
    "memory": "free -m",
    "disk": "df -h"
}

def run_remote_command(ssh,command):
    stdin,stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode()

def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=HOST, username=USERNAME,key_filename=KEY_FILE)

    results ={}
    for key,cmd in COMMANDS.items():
        results[key] = run_remote_command(ssh,cmd)

    ssh.close()

    #SAve to Json file
    os.makedirs("output", exist_ok=True)
    filename = f"output/health_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename,"w") as f:
        json.dump(results,f,indent=4)

    print (f"Health check saved to {filename}")

if __name__ == "__main__":
    main()
