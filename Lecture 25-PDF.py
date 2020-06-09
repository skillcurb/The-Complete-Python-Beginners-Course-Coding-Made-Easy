#import module here
import PyPDF2

pdf_file = open('SVM.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

print(pdf_reader.numPages)

page = pdf_reader.getPage(3)

print(page.extractText())

pdf_file.close()