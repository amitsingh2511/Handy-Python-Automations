import PyPDF2
 
#create file object variable
#opening method will be rb
pdffileobj=open('Admit Card.pdf','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
#This will store the number of pages of this pdf file
x=pdfreader.numPages
text = ""
#create a variable that will select the selected number of pages
for i in range(pdfreader.numPages):
    current_page = pdfreader.getPage(i)
#create text variable which will store all text datafrom pdf file
    text+=current_page.extractText()
#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"
file1=open(r"D:/My project/Handy-Python-Automations/amit.txt","a")
file1.writelines(text)

# closing the pdf file object
pdffileobj.close()
# closing the text file object
file1.close()