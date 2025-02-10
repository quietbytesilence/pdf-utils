import os
import PyPDF2
from PyPDF2 import PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re

def create_footer_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.drawString(30, 20, text)
    c.save()

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def merge_pdfs(output_filename="output.pdf"):
    folder_path = os.getcwd()
    merger = PyPDF2.PdfMerger()
    
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")], key=natural_sort_key)
    
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return
    
    output_path = os.path.join(folder_path, output_filename)
    writer = PyPDF2.PdfWriter()
    
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        print(f"Adicionando: {pdf_path}")
        
        reader = PyPDF2.PdfReader(pdf_path)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            footer_filename = os.path.join(folder_path, "footer.pdf")
            create_footer_pdf(f"Arquivo: {pdf}", footer_filename)
            footer_reader = PyPDF2.PdfReader(footer_filename)
            footer_page = footer_reader.pages[0]
                        page.merge_page(footer_page)
            writer.add_page(page)    
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)    
    print(f"PDFs concatenados em: {output_path}")

if __name__ == "__main__":
    merge_pdfs()
