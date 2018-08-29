import weasyprint
import glob
import os

#pdfkit.from_file('Pandas_1-Introduction.html', 'ye.pdf')


for filename in glob.glob("*.html"):
    #pdfkit.from_file(filename, filename[:-5]+'.pdf')
    weasyprint.HTML(filename).write_pdf(filename[:-5]+'.pdf')


    

