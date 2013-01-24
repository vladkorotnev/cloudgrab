#!/usr/bin/env python
print "CloudApp all item snapshot"
login=raw_input("Login to CloudApp: ")
import getpass
passw=getpass.getpass("Password for CloudApp: ")
from cloudapp.cloud import Cloud
mycloud=Cloud()
mycloud.auth(login,passw)
print "Getting items..."
finished = False
items=[]
cpg=1
while not finished:
	current = mycloud.list_items(page=cpg, per_page=2000)
	if len(current) == 0:
		finished = True;
	for itemDict in current:
		if 'download_url' in itemDict:
			items.append(itemDict['download_url'])
	cpg = cpg + 1
print "Got "+str(len(items))+" items"
import urllib
for url in items:
	webFile = urllib.urlopen(url)
	name = urllib.unquote(urllib.unquote(url.split('/')[-1]))
	print "Downloading \""+name+"\"..."
	localFile = open(name, 'w')
	localFile.write(webFile.read())
	localFile.close()
print "Completed."
print "by vladkorotnev, 2013"