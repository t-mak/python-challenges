##14.7 Unscramble pdf
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path.home() / "OneDrive/Pulpit/scrambled.pdf" #correct reading from my desktop, pulpit not desktop for some reason.
pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

def extract_page(page):
    return page.extractText()

extractedPages = list()
for page in pdf_reader.pages:
    extractedPages.append(page.extractText())
    extractedPages.sort()
    print(extractedPages)

pages = list(pdf_reader.pages) #list of pages
pages.sort(key=extract_page) #key needs to be callable

for page in pages:
    if page["/Rotate"] != 0:
        degrees = page["/Rotate"]
        page.rotateCounterClockwise(degrees)
    #print(page.extractText())
    pdf_writer.addPage(page)

#save
output_path = Path.home() / "OneDrive/Pulpit/unscrambled.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

