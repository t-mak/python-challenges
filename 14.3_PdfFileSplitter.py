from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

class PdfFileSplitter:
    def __init__(self, path):
        self.path = path
        self.pdf_reader = PdfFileReader(str(path))
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
    
    def split(self, breakpoint):
    ##    for n in range(1, breakpoint):
    ##        page = input_pdf.getPage(n)
    ##        writer1.addPage(page)
        for page in self.pdf_reader.pages[1:breakpoint]:
            self.writer1.addPage(page)
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        with Path(str(filename)+"_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)
        with Path(str(filename)+"_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)
    
file_path = Path.home() / "Pride_and_Prejudice.pdf"
pdf_splitter = PdfFileSplitter(file_path)
pdf_splitter.split(150)
pdf_splitter.write("mydoc_split")
