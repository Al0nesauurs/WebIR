import os
for root, dirs, files in os.walk("html"):
    for file in files:
        if file.endswith(".html"):
            urlmap = os.path.join(root, file).split("html/")
            print(urlmap[1])