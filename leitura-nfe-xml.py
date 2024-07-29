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