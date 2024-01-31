import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    categorias = [] # lista vazia para armazenar as categorias
    for produtos in dados:
        if produtos['categoria'] not in categorias:
            categorias.append(produtos['categoria'])
            # ordenar e retornar lista 
    categorias.sort()
    return categorias

    ...

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    categoria.replace(' ', '_')
    produtos_categoria = []
    for produtos in dados:
        if produtos['categoria'] == categoria:
            produtos_categoria.append(produtos)
    return produtos_categoria
    ...
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    produtos_por_categoria = listar_por_categoria(dados, categoria)
    produto_mais_caro = produtos_por_categoria[0]
    for produto in produtos_por_categoria:
        if float(produto['preco']) > float(produto_mais_caro['preco']):
            produto_mais_caro = produto

    return produto_mais_caro


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    produtos_por_categoria = listar_por_categoria(dados, categoria)
    produto_mais_barato = produtos_por_categoria[0]
    for produto in produtos_por_categoria:
        if float(produto['preco']) < float(produto_mais_barato['preco']):
            produto_mais_barato = produto

    return produto_mais_barato


def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    dez_produtos_mais_caros = []
    contador = 10
    while len(dados) > 0:
        produto_mais_caro = dados[0]
        for produto in dados:
            if float(produto['preco']) > float(produto_mais_caro['preco']):
                produto_mais_caro = produto
        dez_produtos_mais_caros.append(produto_mais_caro)
        dados.remove(produto_mais_caro)
        contador -= 1
        if contador == 0:
            break
    return dez_produtos_mais_caros


def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    dez_produtos_mais_baratos = []
    contador = 10
    while len(dados) > 0:
        produto_mais_barato = dados[0]
        for produto in dados:
            if float(produto['preco']) < float(produto_mais_barato['preco']):
                produto_mais_barato = produto
        dez_produtos_mais_baratos.append(produto_mais_barato)
        dados.remove(produto_mais_barato)
        contador -= 1
        if contador == 0:
            break
    return dez_produtos_mais_baratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...

    while True:
        print('1. Listar categorias')
        print('2. Listar produtos de uma categoria')
        print('3. Produto mais caro por categoria')
        print('4. Produto mais barato por categoria')
        print('5. Top 10 produtos mais caros')
        print('6. Top 10 produtos mais baratos')
        print('0. Sair')
        # o imout não precisa dar enter
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            print(listar_categorias(dados))
        elif opcao == 2:
            categoria = input('Digite a categoria desejada: ')
            print(listar_por_categoria(dados, categoria))
        elif opcao == 3:
            categoria = input('Digite a categoria desejada: ')
            print(produto_mais_caro(dados, categoria))
        elif opcao == 4:
            categoria = input('Digite a categoria desejada: ')
            print(produto_mais_barato(dados, categoria))
        elif opcao == 5:
            print(top_10_caros(dados))
        elif opcao == 6:
            print(top_10_baratos(dados))
        elif opcao == 0:
            break
        else:
            print('Opção inválida!')


# Programa Principal - não modificar!
d = obter_dados()
menu(d)
