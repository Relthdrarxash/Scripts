import paramiko

# Start ssh client
ssh = paramiko.SSHClient()
# Specific parameter for my configuration
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Don't forget to add the creds, the ip and the port
ssh.connect("", port=, username="", password="")
# I got 6 fans 
for i in range(6) :
    # Ilo fans value is 0-255 range
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f'fan p {i} max 30')
    
# To do : Make a class if needed to improve the capabilities    
