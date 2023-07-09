# PyPDF2 to manage PDF files.
# PyPDF2 is a library of management of PDF files, made in pure Python,
# free and open code.
# It is possible to read, manipulate, write, and join
# PDF files data.
# Doc: https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_PATH = Path(__file__).parent
PDF_PATH = ROOT_PATH / 'Pdfs'
PDF_FILE = PDF_PATH / 'Livro_ordem.pdf'

MODIFIED_PDFS = ROOT_PATH / 'Modified_pdfs'

MODIFIED_PDFS.mkdir(exist_ok=True)

reader = PdfReader(PDF_FILE)

# print(len(reader.pages))

page0 = reader.pages[0]
image0 = page0.images[0]
print(page0.extract_text())
print(page0.images)

# save image
# with open(MODIFIED_PDFS/image0.name, 'wb') as image:
#     image.write(image0.data)

pdf_files = []
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    if i in [1, 3, 4]:
        continue
    if i == 7:
        break

    with open(MODIFIED_PDFS / f'page{i}.pdf', 'wb') as file:
        pdf_files.append(MODIFIED_PDFS / f'page{i}.pdf')
        writer.add_page(page)
        writer.write(file)


# Create a new pdf with all pages
# with open(MODIFIED_PDFS / 'Novo_Livro.pdf', 'wb') as file:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(file)

merger = PdfMerger()

for file in pdf_files:
    merger.append(file)

merger.write(MODIFIED_PDFS / 'livro_intro.pdf')
merger.close()
