from bs4 import BeautifulSoup
from urllib import urlopen

page=urlopen("http://electionaffairs.com/states/himachal.html").read()
soup=BeautifulSoup(page)

india=[]
for items in soup.findAll("table",attrs={'cellpadding':"4","cellspacing":"4"}):
   for data in items.findAll("tr"):
       for consti in data.findAll("td"):
         for cons in consti.findAll("a"):        
           india.append(cons.get_text())
print india
f=open("constit.py", 'a+')
for item in india:
  f.write("'%s',\n" % item)

f.close()
