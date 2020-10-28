# Download all textures from TextureHaven

# Importing Modules
import requests
import os
from sys import argv
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlretrieve
from urllib.request import URLopener
from fake_useragent import UserAgent

# Arguments
name, resolution, category, fileformat = argv

#File Count
filesnum = 0

print(f"Resolution {resolution}")
print(f"Category: {category}")
print(f"Format: {fileformat}")

ua = UserAgent()
opener = URLopener()
opener.addheader('User-Agent', ua.chrome)

url = 'https://texturehaven.com/textures/'
url_category = url + '?c=' + category

r = requests.get(url_category, allow_redirects=True, headers={'User-Agent': ua.chrome})
soup = BeautifulSoup(r.text, 'html.parser')

save_to = category+' Texture ' + resolution

try:
    os.mkdir(save_to)
except Exception as e:
    pass
os.chdir(save_to)

texs = soup.select('#item-grid a')

for tex in texs:
    href = urlparse(tex['href'])
    filename = href.query[2:]
    new_filename = filename.replace(category+'&t=','')
    dl_url = (f"https://texturehaven.com/files/textures/zip/{resolution}/{new_filename}/{new_filename}_{resolution}_{fileformat}.zip")
    
    print(f"\n{dl_url}")

    try:
        print(f"{new_filename} downloading...")
        opener.retrieve(dl_url, os.path.basename(dl_url))
        filesnum+=1
    except Exception as e:
        print(f"{new_filename} download failed, Continuing...")
        continue

print(f"\nDownload completed. {filesnum} files downloaded.")
