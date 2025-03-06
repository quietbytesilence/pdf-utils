# Utilitários de PDF para Ciência de Dados e Hobby

Bem-vindo ao meu repositório de utilitários de PDF! Aqui, eu compartilho ferramentas que desenvolvo para agilizar meu trabalho como cientista de dados e também por hobby. Esses scripts são projetados para automatizar tarefas comuns relacionadas a PDFs, como busca de termos, extração de dados e geração de relatórios.

---

## Ferramentas Disponíveis

### 1. **Buscador de Termos em PDFs**
   - **Descrição**: Um script Python para buscar termos específicos em arquivos PDFs e gerar um novo PDF com as páginas onde os termos foram encontrados, destacando as ocorrências.
   - **Funcionalidades**:
     - Busca termos individuais ou combinados (usando `&`).
     - Processa múltiplos PDFs em paralelo.
     - Gera um PDF de saída com as páginas relevantes.
       
### 2. **Concatenador de PDFs com Rodapé Personalizado**
   - **Descrição**: Um script Python para concatenar vários PDFs em um único arquivo, adicionando um rodapé personalizado em cada página com o nome do arquivo original.
   - **Funcionalidades**:
     - Concatena PDFs em ordem natural (ex: `arquivo1.pdf`, `arquivo2.pdf`, ...).
     - Adiciona um rodapé personalizado em cada página com o nome do arquivo original.
     - Gera um único PDF de saída.
    
### 3. **Gerador de Relatórios Personalizado**
   - **Descrição**: Um script Python para contabilizar um acervo volumoso de arquivos pdf's
   - **Funcionalidades**:
     - Lê a quantidade de páginas de cada aquivo dentro da pasta de execução _caminha por todas as subpastas_
     - Gera um relatório txt com a quantidade de páginas por arquivo e a quantidade total de páginas

### 4. **Em Breve: Gerador de Relatórios em PDF**
   - **Descrição**: Um script para gerar relatórios em PDF a partir de dados estruturados (CSV, Excel, etc.).
   - **Funcionalidades**:
     - Cria relatórios com gráficos e tabelas.
     - Personalização de layout e estilo.
   - **Status**: Em planejamento.

---

## Como Usar

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/quietbytesilence/pdf-utils.git
   cd pdf-utils
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Buscador de Termos em PDFs

### Visão Geral

O **Buscador de Termos em PDFs** é uma ferramenta Python que permite buscar termos específicos em arquivos PDFs. Ele é útil para:
- Pesquisar palavras-chave em grandes volumes de documentos.
- Gerar um PDF consolidado com as páginas onde os termos foram encontrados.
- Destacar as ocorrências dos termos no PDF de saída.

### Como Usar

1. Crie um arquivo de texto (`wordlist.txt`) com os termos de busca, um por linha. Exemplo:
   ```
   Python
   Machine Learning
   IA & Inteligência Artificial
   ```

2. Execute o script:
   ```bash
   python buscador_pdfs.py -w wordlist.txt -p /caminho/para/pdfs -o resultado.pdf
   ```

   #### Argumentos:
   - `-w` ou `--wordlist`: Arquivo de texto com os termos de busca (obrigatório).
   - `-p` ou `--path`: Diretório onde os PDFs estão armazenados (padrão: diretório atual).
   - `-o` ou `--output`: Nome do arquivo PDF de saída (padrão: `Resultados_DATA_HORA.pdf`).

3. Verifique o arquivo `resultado.pdf` para ver as páginas com os termos destacados.


---
## Concatenador de PDFs com Rodapé Personalizado

### Visão Geral

O **Concatenador de PDFs com Rodapé Personalizado** é uma ferramenta Python que permite:
- Concatenar vários PDFs em um único arquivo.
- Adicionar um rodapé personalizado em cada página com o nome do arquivo original.

### Como Usar

1. Coloque todos os PDFs que deseja concatenar na mesma pasta do script.

2. Execute o script:
   ```bash
   python concatenador.py
   ```

   #### Saída:
   - Um arquivo chamado `output.pdf` será gerado na mesma pasta, contendo todos os PDFs concatenados.
   - Cada página terá um rodapé com o nome do arquivo original.

### Exemplo

Se você tiver os arquivos `arquivo1.pdf`, `arquivo2.pdf` e `arquivo3.pdf` na pasta, o script gerará um único PDF (`output.pdf`) com todas as páginas desses arquivos, e cada página terá um rodapé como:
```
Arquivo: arquivo1.pdf
```

### Visão Geral

Este script Python é uma ferramenta simples para contar o número de arquivos PDF e o total de páginas em um diretório específico. Ele gera um relatório em formato de texto (`relatorio.txt`) com os detalhes de cada livro (nome do arquivo e número de páginas), o número total de livros e o total de páginas.

### Modo de Usar

1. **Instalação de Dependências**: Certifique-se de ter o Python instalado e instale a biblioteca `PyPDF2` se ainda não a tiver:
   ```bash
   pip install PyPDF2
   ```

2. **Execução**: Coloque o script no diretório onde estão os arquivos PDF ou especifique o diretório desejado ao chamar a função `criar_relatorio`. Execute o script:
   ```bash
   python nome_do_script.py
   ```

3. **Resultado**: Um arquivo `relatorio.txt` será gerado no mesmo diretório, contendo as informações sobre os PDFs encontrados.

### Funcionalidades

- **Contagem de PDFs**: O script percorre o diretório especificado (e um nível de subpastas) e conta quantos arquivos PDF estão presentes.
- **Contagem de Páginas**: Para cada PDF encontrado, o script conta o número de páginas usando a biblioteca `PyPDF2`.
- **Geração de Relatório**: As informações coletadas são salvas em um arquivo de texto (`relatorio.txt`), que inclui:
  - Nome de cada arquivo PDF e seu número de páginas.
  - Número total de livros (PDFs) encontrados.
  - Número total de páginas somadas de todos os PDFs.

### Observações

- O script limita a busca a apenas um nível de subpastas a partir do diretório especificado. Se precisar de uma busca mais profunda, ajuste a condição `if root != diretorio:`.
- Erros ao processar PDFs (como arquivos corrompidos) são capturados e exibidos no console, sem interromper a execução do script.

### Exemplo de Saída no `relatorio.txt`:

```
Detalhes dos Livros:
- livro1.pdf: 120 páginas
- livro2.pdf: 85 páginas

Número de livros: 2
Total de páginas: 205
```

Essa ferramenta é útil para quem precisa organizar ou analisar coleções de PDFs, como bibliotecas digitais, materiais de estudo, etc.


## Contribuição

Contribuições são bem-vindas! Se você tem ideias para novas ferramentas ou melhorias nas existentes, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Próximas Ferramentas

Estou constantemente desenvolvendo novas ferramentas para facilitar o trabalho com PDFs. Aqui estão algumas que estão no pipeline:

- **OCR Automatizado**: Integração com ferramentas de OCR para extrair texto de PDFs escaneados.
  - _Provavelmente usando uma api do Google Chrome_

Fique de olho neste repositório para atualizações!

---

## Contato

Se você tiver alguma dúvida, sugestão ou quiser colaborar, sinta-se à vontade para entrar em contato:

- **Telegram**: [@lievasomal](https://t.me/lievasomal)

