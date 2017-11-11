from bs4 import BeautifulSoup
import urllib2

urlmap = open( "./spiders/urlmap.txt", "r" )
webgraph = open( "./webgraphRESERVED.txt", "w" )

urlline = [] 
path = []
i = 0
for line in urlmap:
    urlline.append(line)
    urlline[i]=urlline[i].rstrip()        
    # print(urlline[i])
    i+=1
urlmap.close()

NumUrlOut = []
for i in range (len(urlline)):
  f = open("./spiders/html/"+urlline[i])
  temp = urlline[i].split('/')
  temp[len(temp)-1] = ''
  UrlPath = ""
  for j in range (len(temp)-1) :
      UrlPath += temp[j] + '/'
  print(UrlPath)
  path.append(UrlPath)
  soup = BeautifulSoup(f, 'html.parser')
  chklink = []
  for link in soup.find_all('a'):
      if (link.get('href')):
          temp = link.get('href').split('/')
          chklink.append(temp[len(temp)-1])
          

  if len(chklink) != 0:
    for k in range (len(chklink)):
      if (len(chklink[k])> 0 and chklink[k][0] == '/'):
          chklink[k] = chklink[k][1:]

      if chklink[k] in urlline or path[i].rstrip()+chklink[k] in urlline:
          if (str(urlline.index(path[i].rstrip()+chklink[k])+1) not in NumUrlOut) :
            NumUrlOut.append(str(urlline.index(path[i].rstrip()+chklink[k])+1))
          print(NumUrlOut)
          print("IN HTML "+ urlline[i])
          print("OUT HTML : " + str(urlline.index(path[i].rstrip()+chklink[k])+1) + " " + path[i].rstrip()+chklink[k])
    NumUrlOut.sort()    
    webgraph.write(str(i+1) + " : " + str(NumUrlOut) + "\n")
    NumUrlOut = []       
 
