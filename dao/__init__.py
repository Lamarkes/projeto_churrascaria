from flask import *


def verificar_login(nome, senha):
    if nome == 'Lamark' and senha == '123456':
        return render_template('verificado.html')
    else:
        return False


def salvar_pedido(nome_pedido, tamanho_pedido, qtde_arroz,qtde_feijao, proteina):

    with open('pedidos_salvos/pedidos.txt', 'a') as file:
        file.write(f'\nNumero: {nome_pedido},\n Tamanho do Pedido: {tamanho_pedido},\n Quantidade de Arroz: {qtde_arroz},\n'
                   f'Quantidade de feijão: {qtde_feijao},\n Proteina: {proteina}\n')
