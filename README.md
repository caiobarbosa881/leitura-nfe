Extrator de Informações de NF-e
Este projeto é um script em Python que extrai informações específicas de um arquivo XML de Nota Fiscal Eletrônica (NF-e). Utilizando a biblioteca xml.etree.ElementTree, o script busca e imprime o número da NF-e, o CNPJ do emitente, a descrição do produto e o valor total da NF-e.

Requisitos
Python 3.x
Arquivo XML da NF-e
Como usar
Clone o repositório ou copie o código do script para o seu ambiente de desenvolvimento.
git clone https://github.com/caiobarbosa881/leitura-nfe.git

Certifique-se de ter o arquivo XML da NF-e disponível.

Modifique a linha onde o arquivo XML é carregado para corresponder ao nome do seu arquivo XML:

python
Copiar código
tree = ET.parse("modelo-nf-e.xml")  # Altere para o nome do seu arquivo XML
Execute o script. O script irá buscar as seguintes informações e imprimi-las:

Número da NF-e
CNPJ do emitente
Descrição do produto
Valor total da NF-e
Código do Script
python
Copiar código
import xml.etree.ElementTree as ET

# Carregar o XML
tree = ET.parse("modelo-nf-e.xml")  # Altere para o nome do seu arquivo XML
root = tree.getroot()

# Definir o namespace
nsNFE = {'nfe': "http://www.portalfiscal.inf.br/nfe"}

# Extrair o número da nota fiscal
numero_nfe = root.find('nfe:infNFe/nfe:ide/nfe:nNF', namespaces=nsNFE)
if numero_nfe is not None:
    print(f"Numero da NF-e: {numero_nfe.text}")
else:
    print("Número da NF-e não encontrado.")

# Extrair o CNPJ do emitente
cnpj_emitente = root.find('nfe:infNFe/nfe:emit/nfe:CNPJ', namespaces=nsNFE)
if cnpj_emitente is not None:
    print(f"CNPJ do Emitente: {cnpj_emitente.text}")
else:
    print("CNPJ do Emitente não encontrado.")

# Extrair a descrição do produto
descricao_produto = root.find('nfe:infNFe/nfe:det/nfe:prod/nfe:xProd', namespaces=nsNFE)
if descricao_produto is not None:
    print(f"Descrição do Produto: {descricao_produto.text}")
else:
    print("Descrição do Produto não encontrada.")

# Extrair o valor total da NF-e
valor_total = root.find('nfe:infNFe/nfe:total/nfe:ICMSTot/nfe:vNF', namespaces=nsNFE)
if valor_total is not None:
    print(f"Valor Total da NF-e: {valor_total.text}")
else:
    print("Valor Total da NF-e não encontrado.")
Notas
Certifique-se de que o XML está no formato esperado e contém os elementos necessários.
Os namespaces devem estar corretamente definidos para que o ElementTree consiga localizar os elementos no XML.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
