import PyPDF2
from PyPDF2 import PdfFileReader

pdf = open("Chuong2_input_sample.pdf", "rb")
pdf_reader = PdfFileReader(pdf)
print("So trang trong file pdf:", pdf_reader.pages)
page = pdf_reader.numpages[0]

file_create = open(r"C:\Users\Admin\Desktop\PDFtoTXT\Chuong2_input_sample_txt.txt", "a")
file_create.writelines(text)
pdf.close()