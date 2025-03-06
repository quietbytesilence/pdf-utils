import os
from PyPDF2 import PdfReader

def contar_pdfs_e_paginas(diretorio="."):
    detalhes_livros = []
    num_livros = 0
    total_paginas = 0

    for root, dirs, files in os.walk(diretorio):
        if root != diretorio:  # Limitar a busca a apenas 1 nível de subpastas
            continue

        for file in files:
            if file.lower().endswith(".pdf"):  # Verificar extensão do arquivo
                caminho_pdf = os.path.join(root, file)
                try:
                    leitor = PdfReader(caminho_pdf)
                    num_paginas = len(leitor.pages)
                    detalhes_livros.append((file, num_paginas))
                    total_paginas += num_paginas
                    num_livros += 1
                except Exception as e:
                    print(f"Erro ao processar {file}: {e}")

    return detalhes_livros, num_livros, total_paginas

def criar_relatorio(diretorio="."):
    detalhes_livros, num_livros, total_paginas = contar_pdfs_e_paginas(diretorio)

    caminho_relatorio = os.path.join(diretorio, "relatorio.txt")
    with open(caminho_relatorio, "w", encoding="utf-8") as arquivo:
        arquivo.write("Detalhes dos Livros:\n")
        for nome, paginas in detalhes_livros:
            arquivo.write(f"- {nome}: {paginas} páginas\n")
        arquivo.write("\n")
        arquivo.write(f"Número de livros: {num_livros}\n")
        arquivo.write(f"Total de páginas: {total_paginas}\n")

    print(f"Relatório criado: {caminho_relatorio}")

if __name__ == "__main__":
    criar_relatorio()
