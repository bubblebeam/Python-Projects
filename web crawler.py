# a simple web crawler
# extract the 18th link on the page and follow the link. Repeat this procedure 7 times. print the last url.
# start URL is http://py4e-data.dr-chuck.net/known_by_Hector.html
import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
for i in range(1,8):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    cnt=0
    for tag in tags:
           if cnt==18:break
           url=tag.get('href', None)
           cnt=cnt+1     
print url
