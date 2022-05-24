import PyPDF2

file = open('example.pdf', 'rb')
file_reader = PyPDF2.PdfFileReader(file)
page_obj = file_reader.getPage(0)
print(page_obj.extractText())
file.close()
