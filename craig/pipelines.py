import os
import hashlib
class CraigPipeline(object):
    def process_item(self, item, spider):
        file_name = item['url_to'] #chose whatever hashing func works for you  
        concat = ""
        html =''
        i = 0
        for i in range (0, len(file_name.split("//")[-1].split("/"))):
          if i+1 == len(file_name.split("//")[-1].split("/")):
            html+=file_name.split("//")[-1].split("/")[i]
            break
          concat+=file_name.split("//")[-1].split("/")[i] + '/'
          i+=1
        if not os.path.exists('files/'+concat):
          os.makedirs('files/'+concat)
        if (".html" or ".htm") in html:
          with open('files/%s' % (concat + html), 'a') as f:
              f.write(item['html'])
              f.close()
        if html == 'robot.txt':
          if not os.path.exists('files/robot/'+concat):
            os.makedirs('files/robot/'+concat)
            with open('files/robot/%s' % (concat + html), 'a') as f:
                f.write(item['html'])
                f.close()

