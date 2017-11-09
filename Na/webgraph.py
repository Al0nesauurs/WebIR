from bs4 import BeautifulSoup
import urllib2

urlmap = open( "./spiders/urlmap.txt", "r" )
urlline = [] 
path = []
for line in urlmap:
    urlline.append(line)
for i in range (len(urlline)):
    urlline[i]=urlline[i].rstrip()        
    print(urlline[i])
urlmap.close()

f = open("./spiders/html/"+urlline[0].rstrip())
temp = urlline[0].split('/')
temp[len(temp)-1] = ''
UrlPath = ""
for i in range (len(temp)-1) :
    UrlPath += temp[i] + '/'
soup = BeautifulSoup(f, 'html.parser')
i = 0
chklink = []
for link in soup.find_all('a'):
    if link.get('href')[len(link.get('href'))-1] == 'l':
      print(link.get('href'))
      chklink.append(link.get('href'))
    

print (chklink[0])
if chklink[0] in urlline or UrlPath+chklink[0] in urlline:
    print ("YAY")
else:
    print ("NAY")