## Online Computer and Laptop Store - Unauthenticated File Upload  
**Date:** 5/27/2023  
**Exploit Author:** Alex Gan  
**Vendor Homepage:**  https://www.sourcecodester.com/php/16397/online-computer-and-laptop-store-using-php-and-mysql-source-code-free-download.html?utm_content=cmp-true  
**Software Link:** https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-ocls.zip  
**Version:** v1.0  
**Tested on:** LAMP Fedora server 38 (Thirty Eight) Apache/2.4.57 10.5.19-MariaDB PHP 8.2.6  
**CVE:** CVE-2023-31857  
**References:** https://nvd.nist.gov/vuln/detail/CVE-2023-31857  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://www.exploit-db.com/exploits/51358  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://github.com/Jadore147258369/php-ocls  
### Description:
The **"Online store for computers and laptops"** web application contains a vulnerability in the **"SystemSettings.php"** file that allows unauthorized downloading of the file and execution of arbitrary code on the server. The application does not clear the **"img"** setting when sending data to **"SystemSettings.php?f=update_settings"**, allowing attackers to download and execute files on the server.