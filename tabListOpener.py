import os

cmd=["firefox"]

with open('url_list.txt', 'r') as url_file:
    for url in url_file:
        cmd.append(url.strip())
    
os.system(' '.join(cmd))