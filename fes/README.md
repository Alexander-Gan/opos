## Faculty Evaluation System 1.0 - Unauthenticated File Upload  
**Date:** 5/29/2023  
**Exploit Author:** Alex Gan  
**Vendor Homepage:** https://www.sourcecodester.com/php/14635/faculty-evaluation-system-using-phpmysqli-source-code.html  
**Software Link:** https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-ocls.zip  
**Version:** v1.0  
**Tested on:** LAMP Fedora server 38 (Thirty Eight) Apache/2.4.57 10.5.19-MariaDB PHP 8.2.6  
**CVE:** CVE-2023-33440  
**References:** https://nvd.nist.gov/vuln/detail/CVE-2023-33440  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://www.exploit-db.com/exploits/49320  
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; https://github.com/F14me7wq/bug_report/tree/main/vendors/oretnom23/faculty-evaluation-system  
### Description:
The **"Faculty Evaluation System"** web application contains a vulnerability in the **"ajax.php"** file that allows attackers to upload and execute arbitrary code on the server. This vulnerability occurs due to incorrect handling of the **"img"** parameter when submitting data to **"ajax.php?action=save_user"**.
