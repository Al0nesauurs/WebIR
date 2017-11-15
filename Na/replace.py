with open('webgraph.txt', 'r') as infile,open('testout.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("[]" ,"-1")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace(",", "")

    outfile.write(data)
    # Use testout.txt to preserve webgraph.txt in case of some error happen or file corrupted