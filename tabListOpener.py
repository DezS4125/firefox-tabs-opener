import os
import webbrowser

os.system("firefox")

with open('url_list.txt', 'r') as url_file:
    for url in url_file:
        webbrowser.open(url)