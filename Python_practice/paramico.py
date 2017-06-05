import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.50.35",username = "root",password = "Nexii@123")
stdin, stdout, stderr = ssh.exec_command("ls")


print stdout.read()
stdin.close()
    
