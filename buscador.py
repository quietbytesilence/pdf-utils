import os
import fitz  # PyMuPDF
import re
import argparse
from datetime import datetime
from tqdm import tqdm  # Importando a biblioteca tqdm

def carregar_termos(arquivo_termos):
    """Carrega os termos de busca do arquivo especificado."""
    with open(arquivo_termos, 'r', encoding='utf-8') as f:
        termos = [line.strip() for line in f if line.strip()]
    keywords_individuais = [termo for termo in termos if '&' not in termo]
    keywords_combinados = [termo.split('&') for termo in termos if '&' in termo]
    return keywords_individuais, keywords_combinados

def buscar_termos_em_pdf(caminho_pdf, keywords_individuais, keywords_combinados):
    """Procura os termos nos PDFs e retorna referências das ocorrências."""
    referencias = []
    
    try:
        doc = fitz.open(caminho_pdf)
    except Exception as e:
        print(f"Erro ao abrir {caminho_pdf}: {e}")
        return []

    for num_pag in range(len(doc)):
        try:
            pagina = doc.load_page(num_pag)
            texto = pagina.get_text()

            for palavra in keywords_individuais:
                padrao = re.compile(re.escape(palavra), re.IGNORECASE)
                for match in padrao.finditer(texto):
                    referencias.append({
                        'arquivo': caminho_pdf, 'pagina': num_pag,
                        'palavra': palavra, 'inicio': match.start(), 'fim': match.end()
                    })

            for combinacao in keywords_combinados:
                termos_combinados = [termo.strip() for termo in combinacao]
                if all(re.search(re.escape(termo), texto, re.IGNORECASE) for termo in termos_combinados):
                    referencias.append({
                        'arquivo': caminho_pdf, 'pagina': num_pag,
                        'palavra': ' & '.join(termos_combinados),
                        'inicio': 0, 'fim': 0
                    })
        except Exception as e:
            print(f"Erro ao processar página {num_pag + 1} do arquivo {caminho_pdf}: {e}")

    doc.close()
    return referencias

def buscar_em_diretorio(pasta_base, keywords_individuais, keywords_combinados):
    """Percorre a pasta e subpastas buscando PDFs e processando-os."""
    todas_referencias = []
    
    # Lista todos os arquivos PDF na pasta e subpastas
    arquivos_pdf = []
    for raiz, _, arquivos in os.walk(pasta_base):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.pdf'):
                arquivos_pdf.append(os.path.join(raiz, arquivo))

    # Usando tqdm para mostrar a barra de progresso
    for caminho_pdf in tqdm(arquivos_pdf, desc="Processando PDFs", unit="arquivo"):
        referencias = buscar_termos_em_pdf(caminho_pdf, keywords_individuais, keywords_combinados)
        todas_referencias.extend(referencias)

    return todas_referencias

def gerar_pdf_resultado(referencias, nome_saida):
    """Gera um PDF consolidando todas as páginas encontradas com os termos destacados."""
    if not referencias:
        print("\nNenhuma ocorrência encontrada.")
        return

    output_doc = fitz.open()
    print("\nGerando arquivo de resultados...")

    for ref in referencias:
        try:
            doc = fitz.open(ref['arquivo'])
            pagina = doc.load_page(ref['pagina'])
            output_doc.insert_pdf(doc, from_page=ref['pagina'], to_page=ref['pagina'])
            pagina_saida = output_doc[-1]

            if '&' not in ref['palavra']:
                quads = pagina_saida.search_for(ref['palavra'], quads=True)
                for quad in quads:
                    pagina_saida.add_highlight_annot(quad).update()
            else:
                termos_combinados = ref['palavra'].split(' & ')
                for termo in termos_combinados:
                    quads = pagina_saida.search_for(termo, quads=True)
                    for quad in quads:
                        pagina_saida.add_highlight_annot(quad).update()

            doc.close()
        except Exception as e:
            print(f"Erro ao processar referência {ref}: {e}")

    output_doc.save(nome_saida)
    output_doc.close()
    print(f"\nPDF com destaques salvo como: {nome_saida}")

def main():
    parser = argparse.ArgumentParser(description="Buscador de PDFs por palavras-chave.", add_help=False)  
    parser.add_argument("-p", "--path", default=os.getcwd(), help="Diretório onde buscar os PDFs (padrão: diretório atual)")
    parser.add_argument("--help", action="store_true", help="Mostra a ajuda e sai.")
    parser.add_argument("-w", "--wordlist", required=True, help="Arquivo TXT contendo os termos de busca")
    parser.add_argument("-o", "--output", default=f"Resultados_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf", help="Nome do PDF de saída (padrão: 'Resultados_DATA.pdf')")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return

    keywords_individuais, keywords_combinados = carregar_termos(args.wordlist)
    referencias = buscar_em_diretorio(args.path, keywords_individuais, keywords_combinados)
    gerar_pdf_resultado(referencias, args.output)

if __name__ == "__main__":
    main()
