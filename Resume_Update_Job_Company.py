from docxtpl import DocxTemplate
import datetime
from docx2pdf import convert

pos = input("Enter the name of the position: ")
co = input("Enter the company name: ")
context = { 'pos': pos,
            'co': co}
                
import os.path
rootdir = '' # set path to resume folder with .docx file
doc = DocxTemplate(os.path.join(rootdir, '')) # add resume template file name 

# load dictionary references
doc.render(context)

doc.save('Your Name - Resume - ' + co + ' - ' + pos + '.docx') # save as new .docx file with customized name
convert('Your Name - Resume - ' + co + ' - ' + pos + '.docx') # export as PDF
