import os
import hashlib
class NaPipeline(object):
    def process_item(self, item, spider):
        file_name = item['url'] #chose whatever hashing func works for you  
        concat = ""
        html =''
        i = 0
        for i in range (0, len(file_name.split("//")[-1].split("/"))):
          if i+1 == len(file_name.split("//")[-1].split("/")):
            html+=file_name.split("//")[-1].split("/")[i]
            break
          concat+=file_name.split("//")[-1].split("/")[i] + '/'
          i+=1

        if (".html" or ".htm") in html:
          if not os.path.exists('html/'+concat):
            os.makedirs('html/'+concat)
          with open('html/%s' % (concat + html), 'a') as f:
              f.write(item['html'])
              f.close()
        if html == 'robots.txt':
          if not os.path.exists('html/robots/'+concat):
            os.makedirs('html/robots/'+concat)
            with open('html/robots/%s' % (concat + html), 'a') as f:
                f.write(item['html'])
                f.close()

