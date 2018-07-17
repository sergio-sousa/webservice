"""
WEB Services
Integracao de Claudino com @-Extrato (BoaVista)
para fechamento da remessa de venda de cartao de terceiro

Desenvolvimento: Sergio
Mentoria: Milton Filho
"""
# -*- encoding: utf-8 -*-
import xmltodict as xd
import os, json, sys
import requests

def lerArquivo(nome_arq):
    #print('Nome do Arquivo : ', nome_arq)
    # Teste documento
    # print(lerArquivo(sys.argv[1]))
    with open(nome_arq, 'r') as arq:
        texto = arq.readlines()
        #print(texto)
        #print ('Texto ..: ',texto)
        #for linhas in texto:
        #    print('Linhas do Arquivos ..: ', linhas)
    return texto


if __name__ == "__main__":
    # URL de Homologacao
    url = "http://homolog.eextrato.com.br:8181/conciliador/rest/remessa/venda"

    # 0010149970190002 - XPTO
    # dados da venda
    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<VendasERP>\n<venda><id>TED-5072018-2-E-1</id><dataVenda>2018-07-05</dataVenda><nsu>054797</nsu><nsuHost>054797</nsuHost><autorizacao>247028</autorizacao><plano>1</plano><rede>2</rede><bandeira>1</bandeira><produto>D</produto><valor>3391.02</valor><codigoLoja>XPTO</codigoLoja><codigoEstabelecimento></codigoEstabelecimento><areaCliente></areaCliente><status>1</status></venda>\n<venda><id>TED-5072018-4-P-5</id><dataVenda>2018-07-05</dataVenda><nsu>054656</nsu><nsuHost>000054656</nsuHost><autorizacao></autorizacao><plano>6</plano><rede>2</rede><bandeira>4</bandeira><produto>C</produto><valor>1805.50</valor><codigoLoja>000000000300155</codigoLoja><codigoEstabelecimento></codigoEstabelecimento><areaCliente></areaCliente><status>1</status></venda>\n</VendasERP>\n\n\n"
    
    # payload = lerArquivo(sys.argv[1])
    # Codigos de liberacao
    # Atributos que devem ser enviado no cabecalho da requisicao POST
    headers = {
        'chaveAcesso': "a546ec9af4bc9e83e681d45fd412bf58",
        'chaveSecreta': "a421d64167ae0d4493a75cf7f98e09a1c3067338",
        'Content-Type': "application/xml",
        'Cache-Control': "no-cache",
        'Postman-Token': "b964ed42-9279-4576-b71c-2f4f1009f87d"
        }
    
    #lerArquivo(sys.argv[1])
    response = requests.request("POST", url, data=payload, headers=headers)
    row=xd.parse(response.text)

    #print('Primeiro : ',response.text)
    #print('toDict : ', dict(row))
    #print('toDict : ', row.keys())

    if not 'RemessaResponse' in row:
        raise Exception ('Erro Estrutura')

    if 'status' in row['RemessaResponse']:        
        print(row['RemessaResponse']['status'])
   
    if 'vendaERPErro' in row['RemessaResponse']:
        if 'descricao' in row['RemessaResponse']['vendaERPErro']:        
            print(row['RemessaResponse']['vendaERPErro']['descricao'])

    if 'erro' in row['RemessaResponse']:
        if 'descricao' in row['RemessaResponse']['erro']:        
            print(row['RemessaResponse']['erro']['descricao'])


    #print(lerArquivo(sys.argv[1]))

