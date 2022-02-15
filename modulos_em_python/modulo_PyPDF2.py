"""
doc: https://pythonhosted.org/PyPDF2/
"""

import PyPDF2
import os

caminho_dos_pdfs = r'C:\Users\Martin Lucidarme\Dropbox\MEF\Administratif\Notes de frais\fev 2022'
# unindo pdfs
'''
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_file = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_file, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(rf'{caminho_dos_pdfs}\note_de_frais_fev.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
'''

# dividindo pdfs
pdf_juntado = r'C:\Users\Martin Lucidarme\Dropbox\MEF\Administratif\Notes de frais\fev 2022\note_de_frais_fev.pdf'
with open(pdf_juntado, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)  # le o arquivo
    num_paginas = leitor.getNumPages()  # nb paginas totais

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()  # escreve pdfs
        pagina_atual = leitor.getPage(num_pagina)  # pega a página segundo num da pagina em qual ta o for
        escritor.addPage(pagina_atual)  # adiciona a pagina num novo pdf

        with open(caminho_dos_pdfs + rf'\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
