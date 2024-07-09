import os
restaurantes = [{'nome': 'Oliva', 'categoria': 'Pizzaria', 'ativo': False}, 
                {'nome': 'Tamaya', 'categoria': 'Comida Japonesa', 'ativo': False}, 
]

def exibir_nome_programa():
    print('𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastro_restaurante():
    exibir_subtitulo('Cadastro de Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante} que deseja cadastrar: ')
    ativo_restaurante = False
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Parabéns! O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurante():
    exibir_subtitulo('Lista de restaurante')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante_lista = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante_lista.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    restaurante_encontrado = False
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            voltar_ao_menu()
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
    voltar_ao_menu()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '-' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print('')

def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu ')
    main()

def finalizar_app():
    exibir_subtitulo('Encerrando o Aplicativo')

def opcao_invalida():
    exibir_subtitulo('Opção Inválida.')
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()