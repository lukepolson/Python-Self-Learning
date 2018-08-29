import os
delete_list = ["color: #000 !important;"]

for filename in os.listdir('/Users/lukepolson/Documents/Jupyter Tutorials/python/htmls'):
    if filename.endswith(".html"):
        infile = filename
        outfile = filename+'temp'
	
        fin = open(infile)
        fout = open(outfile, "w+")
	
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
                fout.write(line)
                
        fin.close()
        fout.close()
        os.rename(filename+'temp', filename)
	
        continue
    else:
        continue
