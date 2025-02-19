## Multi-Vendor Online Groceries Management System 1.0 - Remote Code Execution  
**Date:** 5/15/2023  
**Exploit Author:** Alex Gan  
**Vendor Homepage:** https://www.sourcecodester.com/php/15166/multi-vendor-online-groceries-management-system-phpoop-free-source-code.html  
**Software Link:** https://www.sourcecodester.com/sites/default/files/download/oretnom23/mvogms_2.zip  
**Version:** v1.0  
**Tested on:** LAMP Fedora server 35 (Thirty Five) Apache/2.4.54 10.5.18-MariaDB PHP 8.0.26  
**References:** https://www.exploit-db.com/exploits/51394  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://www.exploit-db.com/exploits/50739  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://nvd.nist.gov/vuln/detail/CVE-2022-26632  
### Description:
A vulnerability in the **"SystemSettings.php"** file allows injecting arbitrary PHP-code in the presence of the content parameter in the **"POST"** request, the script writes each element of the **"$_POST['content']"** array to files with the **".html"** extension using the **"file_put_contents()"** function. However, the lack of proper validation and sanitization of user input allows an attacker to inject malicious PHP-code that will be executed when the request is processed. 

A vulnerability in the **"home.php"** file could allow the execution of arbitrary PHP-code. The content of the **"welcome.html"** file is included in the code using the **"include()"** function.
