#pdf to text convertion
import PyPDF2
pdfFileObj = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
texts = pageObj.extractText()
print(texts)
