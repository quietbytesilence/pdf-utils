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

### 2. **Em Breve: Extrator de Tabelas de PDFs**
   - **Descrição**: Uma ferramenta para extrair tabelas de PDFs e convertê-las em formatos como CSV ou Excel.
   - **Funcionalidades**:
     - Extrai tabelas de PDFs estruturados.
     - Suporta múltiplas páginas e formatos complexos.
   - **Status**: Em desenvolvimento.

### 3. **Em Breve: Gerador de Relatórios em PDF**
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

Para mais detalhes, consulte a [Documentação Completa do Buscador de Termos em PDFs](docs/buscador-termos.md).

---

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

