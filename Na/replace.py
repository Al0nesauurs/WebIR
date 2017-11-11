with open('test.txt', 'r') as infile,open('testout.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("[]" ,"-1")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace(",", "")

    outfile.write(data)