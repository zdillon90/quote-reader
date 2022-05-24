from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = reader.numPages
page = reader.pages[0]
text = page.extract_text()
print(text)
