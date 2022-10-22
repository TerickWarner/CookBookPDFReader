import PyPDF2

pdfFileObj = open('C:/Users/teric/Desktop/cookbookpdfs/SHL_Cookbook_v3.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# printing number of pages in pdf file
print(pdfReader.numPages)