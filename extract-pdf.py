#! /usr/bin/python3
import PyPDF2

class WorkPDF:
    def __init__(self,pdf_fileName):
        self.self = self
        self.pdf_fileName = pdf_fileName

    def read_PDF(self):
        # We are opening the PDF in read binary mode and storing into file_obj
        file_obj = open(self.pdf_fileName,'rb')

        read_obj = PyPDF2.PdfFileReader(file_obj)

        print(f'Total Page Count: {read_obj.numPages}')

        # We can target a specific page and extract the text
        read_page = read_obj.getPage(2)
        read_page.extractText()

        file_obj.close()
